def naive_topsort(g, s=None):
    if s is None:
        s = set(range(len(g)))
    if len(s) == 1:
        return list(s)
    v = s.pop()
    seq = naive_topsort(g, s)
    min_i = 0
    for i, u in enumerate(seq):
        if v in g[u]:
            min_i += 1
    seq.insert(min_i, v)
    return seq


def main():
    a, b, c, d, e = range(5)
    g = [{c, e}, {}, {b, e}, {b}, {d}]
    seq = naive_topsort(g)
    print(seq)


if __name__ == '__main__':
    main()