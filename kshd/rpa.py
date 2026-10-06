import pickle
import shutil
import zlib


def read_index(path):
    with open(path, 'rb') as f:
        _, offset, key = f.readline().split()[:3]
        offset, key = int(offset, 16), int(key, 16)
        f.seek(offset)
        index = pickle.loads(zlib.decompress(f.read()), encoding='bytes')
    return {(k.decode() if isinstance(k, bytes) else k): (path, v[0][0] ^ key, v[0][1] ^ key, v[0][2] if len(v[0]) > 2 else b'')
            for k, v in index.items()}


def read(entry):
    path, offset, length, prefix = entry
    prefix = prefix.encode('latin1') if isinstance(prefix, str) else prefix
    with open(path, 'rb') as f:
        f.seek(offset)
        return prefix + f.read(length - len(prefix))


def write(f, files, key=0x42424242):
    offset = len(b'RPA-3.0 %016x %08x\n' % (0, key))
    index = {}
    for name in sorted(files):
        index[name.encode()] = [(offset ^ key, files[name][0] ^ key, b'')]
        offset += files[name][0]
    f.write(b'RPA-3.0 %016x %08x\n' % (offset, key))
    for name in sorted(files):
        with files[name][1]() as src:
            shutil.copyfileobj(src, f, 1 << 20)
    f.write(zlib.compress(pickle.dumps(index, 2), 9))
