from .rpyc import dumps, expr, is_node, loads
from .tree import convert, flatten, set_leaf, source, statements, to_scene


class PatchError(Exception):
    pass


def apply(name, data, edits):
    tree = loads(data)
    code = [l for l in flatten(tree) if l.code] if 'code' in edits else []
    for old, new, count in edits.get('code', []):
        if sum(source(l.raw).count(old) for l in code) != count:
            raise PatchError('%s: code not found: %r' % (name, old[:80]))
        for l in code:
            if old in source(l.raw):
                set_leaf(code, l, convert(source(l.raw).replace(old, new), l.raw))
    found = {(label, n, tuple(fp)): node for label, n, fp, node in statements(tree)} if 'nodes' in edits else {}
    targets = [(e, found.get((e['label'], e['n'], tuple(e['match'])))) for e in edits.get('nodes', [])]
    for e, node in targets:
        if node is None:
            raise PatchError('%s: statement not found in label %r: %r' % (name, e['label'], e['match'][:3]))
        if e.get('scene'):
            to_scene(node)
        if 'atl' in e:
            template = next((v for _, v in node.properties if is_node(v, 'PyExpr')), None)
            node.properties = [(k, expr(v, template)) for k, v in e['atl']['properties']]
            for attr in ('duration', 'warper'):
                if attr in e['atl']:
                    setattr(node, attr, convert(e['atl'][attr], getattr(node, attr)))
        if 'set' in e:
            leaves = flatten(node)
            for i, v in e['set']:
                set_leaf(leaves, leaves[i], convert(v, leaves[i].raw))
    return dumps(tree, data)
