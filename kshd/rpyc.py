import copy
import copyreg
import io
import pickle
import sys
import types
import zlib

_classes = {}


def _keys(d):
    return {(k.decode() if isinstance(k, bytes) else k): v for k, v in d.items()}


class Node:
    _cls = None

    def __new__(cls, *args):
        self = object.__new__(cls)
        if args:
            self.__dict__['_args'] = args
        return self

    def __setstate__(self, state):
        self.__dict__['_raw'] = state
        if isinstance(state, dict):
            self.__dict__.update(_keys(state))
        elif isinstance(state, tuple) and len(state) == 2 and all(s is None or isinstance(s, dict) for s in state):
            for s in state:
                self.__dict__.update(_keys(s or {}))
        else:
            self.__dict__['_state'] = state

    def __reduce_ex__(self, protocol):
        d = self.__dict__
        raw = d.get('_raw')

        def rebuild(sd):
            if sd is None:
                return None
            known = {k.decode() if isinstance(k, bytes) else k for k in sd}
            out = {k: d.get(k.decode() if isinstance(k, bytes) else k, v) for k, v in sd.items()}
            out.update({k.encode(): v for k, v in d.items() if k[0] != '_' and k not in known})
            return out

        if raw is None:
            state = None
        elif '_state' in d:
            state = d['_state']
        elif isinstance(raw, dict):
            state = rebuild(raw)
        else:
            state = tuple(rebuild(s) for s in raw)
        args = (type(self),) + tuple(d.get('_args', ()))
        return (copyreg.__newobj__, args) if state is None else (copyreg.__newobj__, args, state)


def cls(module, name):
    key = module + '.' + name
    if key not in _classes:
        _classes[key] = type(name, (Node,), {'_cls': key, '__module__': module, '__qualname__': name})
        parts = module.split('.')
        for i in range(1, len(parts) + 1):
            mod = '.'.join(parts[:i])
            if mod not in sys.modules:
                sys.modules[mod] = types.ModuleType(mod)
                if i > 1:
                    setattr(sys.modules['.'.join(parts[:i - 1])], parts[i - 1], sys.modules[mod])
        setattr(sys.modules[module], name, _classes[key])
    return _classes[key]


def is_node(o, name):
    return isinstance(o, Node) and o._cls.endswith('.' + name)


def expr(text, template):
    if template is None:
        return text
    o = cls('renpy.ast', 'PyExpr')(text, *template._args[1:])
    o.__setstate__(copy.copy(template._raw))
    return o


class _Unpickler(pickle.Unpickler):
    def find_class(self, module, name):
        try:
            return super().find_class(module, name)
        except (ImportError, AttributeError):
            return cls(module, name)


def loads(data):
    return _Unpickler(io.BytesIO(zlib.decompress(data)), encoding='bytes').load()


def dumps(obj, original):
    z = zlib.decompressobj()
    z.decompress(original)
    return zlib.compress(pickle.dumps(obj, 2), 9) + z.unused_data
