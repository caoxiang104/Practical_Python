def find(C, u):
    if C[u] != u:
        C[u] = find(C, C[u])
    return C[u]


def union(C, R, u, v):
    u, v = find(C, u), find(C, v)
    if R[u] > R[v]:
        C[v] = u
    else:
        C[u] = v
    if R[u] == R[v]:
        R[v] += 1


def kruskal(G):
    E = [(G[u][v], u, v) for u in G for v in G[u]]
    T = set()
    C, R = {u: u for u in G}, {u: 0 for u in G}
    E = sorted(E)
    for _, u, v in E:
        if find(C, u) != find(C, v):
            T.add((u, v))
            union(C, R, u, v)
    return T


def main():
    a, b, c, d, e, f = range(6)
    g = {a: {b: 1, c: 2, d: 3, e: 6}, b: {a: 1, c: 2, e: 4}, c: {a: 2, b: 2, d: 2}, d: {a: 3, c: 2, f: 3},
         e: {a: 6, b: 4, f: 2}, f: {d: 3, e: 2}}
    seq = kruskal(g)
    print(seq)


if __name__ == '__main__':
    main()