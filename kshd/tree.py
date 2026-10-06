from .rpyc import Node, cls, expr, is_node

NOISE = {'filename', 'linenumber', 'next', 'name', 'attributes', 'translatable', 'hide', 'store', 'loc', 'location', 'mode'}
LANGS = sorted(['en', 'es', 'fr', 'jp', 'de', 'kr', 'pl', 'pt_br', 'ru', 'zh', 'zh_hant'], key=len, reverse=True)
STATEMENTS = ('RawMultipurpose', 'Show', 'Scene')


def text(v):
    if is_node(v, 'PyExpr'):
        v = v._args[0]
    if isinstance(v, bytes):
        v = v.decode('utf-8', 'replace')
    return ' '.join(v.split()) if isinstance(v, str) else v


def source(v):
    if is_node(v, 'PyExpr'):
        v = v._args[0]
    return v.decode('utf-8') if isinstance(v, bytes) else v


def convert(v, template):
    if is_node(template, 'PyExpr'):
        return expr(v, template)
    if isinstance(template, bytes):
        return v.encode()
    return v


class Leaf:
    __slots__ = ('sig', 'val', 'path', 'raw')

    def __init__(self, sig, val, path, raw):
        self.sig, self.val, self.path, self.raw = sig, val, path, raw

    @property
    def tok(self):
        return self.sig.rsplit('/', 1)[-1] + '=' + repr(self.val)

    @property
    def code(self):
        return self.sig.endswith('/code')


def flatten(o, sig='', out=None, path=()):
    out = [] if out is None else out
    if is_node(o, 'PyExpr'):
        out.append(Leaf(sig, text(o), path, o))
    elif is_node(o, 'PyCode'):
        out.append(Leaf(sig + '/code', text(o._state[1]), path + ((o, None),), o._state[1]))
    elif isinstance(o, Node):
        name = o._cls.rsplit('.', 1)[1]
        out.append(Leaf(sig + '/' + name, '<node>', path, o))
        for k in sorted(o.__dict__):
            v = o.__dict__[k]
            if k[0] != '_' and k not in NOISE and v is not None and v is not False and v != []:
                flatten(v, sig + '/' + name + '.' + k, out, path + ((o, k),))
        if name == 'Label':
            out.append(Leaf(sig + '/Label.name', text(o.name), path + ((o, 'name'),), o.name))
    elif isinstance(o, dict):
        for k in sorted(o, key=repr):
            flatten(o[k], sig + '{}', out, path + ((o, k),))
    elif isinstance(o, (list, tuple)):
        for i, v in enumerate(o):
            flatten(v, sig + ('[]' if isinstance(o, list) else '()'), out, path + ((o, i),))
    elif o is not None:
        out.append(Leaf(sig, text(o), path, o))
    return out


def set_leaf(leaves, leaf, value):
    val = value
    for c, k in reversed(leaf.path):
        if isinstance(c, tuple):
            new = c[:k] + (val,) + c[k + 1:]
            for l in leaves:
                if any(x is c for x, _ in l.path):
                    l.path = tuple((new if x is c else x, y) for x, y in l.path)
            val = new
            continue
        if k is None:
            c._state = (c._state[0], val) + c._state[2:]
        elif isinstance(c, Node):
            c.__dict__[k] = val
        else:
            c[k] = val
        break
    leaf.raw, leaf.val = value, text(value)


def label_key(name):
    for lang in LANGS:
        if name.startswith(lang + '_'):
            return name[len(lang) + 1:]
        if name.endswith('_' + lang):
            return name[:-len(lang) - 1]
    return name


def fingerprint(node):
    return [l.tok for l in flatten(node) if '.atl' not in l.sig]


def statements(tree):
    label, seen, out = '', {}, []
    for l in flatten(tree):
        if l.val != '<node>':
            continue
        if is_node(l.raw, 'Label'):
            label = label_key(text(l.raw.name))
        elif l.raw._cls.rsplit('.', 1)[1] in STATEMENTS:
            fp = fingerprint(l.raw)
            key = (label, tuple(fp))
            out.append((label, seen.get(key, 0), fp, l.raw))
            seen[key] = seen.get(key, 0) + 1
    return out


def to_scene(node):
    node.__class__ = cls('renpy.ast', 'Scene')
    node.layer = b'master'
