def naive_find(C, u):
    while C[u] != u:
        u = C[u]
    return u


def naive_union(C, u, v):
    u = naive_find(C, u)
    v = naive_find(C, v)
    C[u] = v


def naive_kruskal(G):
    E = [(G[u][v], u, v) for u in G for v in G[u]]
    T = set()
    C = {u:u for u in G}
    E = sorted(E)
    for _, u, v in E:
        if naive_find(C, u) != naive_find(C, v):
            T.add((u, v))
            naive_union(C, u, v)
    return T


def main():
    a, b, c, d, e, f = range(6)
    g = {a:{b:1, c:2, d:3, e:6}, b:{a:1, c:2, e:4}, c:{a:2, b:2, d:2}, d:{a:3, c:2, f:3}, e:{a:6, b:4, f:2}, f:{d:3, e:2}}
    seq = naive_kruskal(g)
    print(seq)


if __name__ == '__main__':
    main()