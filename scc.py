from dfs_topsort import dfs_topsort


def walk(G, s, S=set()):
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P, S):
            Q.add(v)
            P[v] = u
    return P


def tr(G):
    GT = {}
    for u in range(len(G)): GT[u] = set()
    for u in range(len(G)):
        for v in G[u]:
            GT[v].add(u)
    return GT


def scc(G):
    GT = tr(G)
    sccs, seen = [], set()
    for u in dfs_topsort(G):
        if u in seen: continue
        C = walk(GT, u, seen)
        seen.update(C)
        sccs.append(C)
    return sccs


def main():
    a, b, c, d, e, f, g, h, i = range(9)
    g = [[b, c], [d, e, i], [d], [a, h], [f], [g], [e, h], [i], [h]]
    print(scc(g))


if __name__ == '__main__':
    main()