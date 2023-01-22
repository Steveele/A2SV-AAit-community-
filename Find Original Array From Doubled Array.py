
out = collections.Counter(changed)
if out[0] % 2: return []
    for c in sorted(out):
        if out[c] > out[c*2]:
            return []
        out[c*2] -= out[c] if c else coll[c] // 2
        return list(out.elements())


