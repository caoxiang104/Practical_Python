def iter_dfs(G, s):
    S, Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S: continue
        S.add(u)
        Q.extend(G[u])
        yield u


def main():
    a, b, c, d, e, f, g, h = range(8)
    g = [[b, c, d, e, f], [c, e], [d], [e], [f], [g, h], [f, h], [f, g]]
    print(list(iter_dfs(g, a)))


if __name__ == '__main__':
    main()