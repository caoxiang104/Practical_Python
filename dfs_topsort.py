def dfs_topsort(G):
    S, res = set(), []

    def recurse(u):
        if u in S: return
        S.add(u)
        for v in G[u]:
            recurse(v)
        res.append(u)

    for u in range(len(G)):
        recurse(u)
    res.reverse()
    return res


def main():
    a, b, c, d, e, f, g, h = range(8)
    g = [[b, c, d, e, f], [c, e], [d], [e], [f], [g, h], [f, h], [f, g]]
    # print(g)
    print(dfs_topsort(g))


if __name__ == '__main__':
    main()