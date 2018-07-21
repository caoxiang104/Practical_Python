from collections import defaultdict


def dfs(G, s, d, f, S=None, t=0):
    if S is None: S = set()
    d[s] = t; t += 1
    S.add(s)
    for u in G[s]:
        if u in S: continue
        t = dfs(G, u, d, f, S, t)
    f[s] = t; t += 1
    return t


def main():
    a, b, c, d, e, f, g, h = range(8)
    g = [[b, c, d, e, f], [c, e], [d], [e], [f], [g, h], [f, h], [f, g]]
    d = defaultdict()
    f = defaultdict()
    print(dfs(g, a, d, f))
    print(d)
    print(f)


if __name__ == '__main__':
    main()