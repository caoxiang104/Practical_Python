def rec_dfs(G, s, S=None):
    if S is None: S = list()
    S.append(s)
    for u in G[s]:
        if u in S: continue
        rec_dfs(G, u, S)
    return S


def main():
    a, b, c, d, e, f, g, h = range(8)
    g = [[b, c, d, e, f], [c, e], [d], [e], [f], [g, h], [f, h], [f, g]]
    print(rec_dfs(g, a))


if __name__ == '__main__':
    main()