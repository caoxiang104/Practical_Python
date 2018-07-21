def iddfs(G, s):
    yielded = set()

    def recurse(G, s, d, S=None):
        if s not in yielded:
            yield s
            yielded.add(s)
        if d == 0: return
        if S is None: S = set()
        S.add(s)
        for u in G[s]:
            if u in S: continue
            for v in recurse(G, u, d-1, S):
                yield v
    n = len(G)
    for d in range(n):
        if len(yielded) == n: break
        for u in recurse(G, s, d):
            yield u


def main():
    a, b, c, d, e = range(5)
    g = [[d], [a, c], [d, e], [e], []]
    print(list(iddfs(g, a)))


if __name__ == '__main__':
    main()