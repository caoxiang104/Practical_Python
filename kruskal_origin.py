def kruskal(G):
    E = [(G[u][v], u, v) for u in G for v in G[u]]
    T = set()
    vertex = set()
    E = sorted(E)
    for _, u, v in E:
        if len(T) == len(G) - 1:
            return T
        else:
            if u and v in vertex:
                continue
            else:
                T.add((u, v))
                if u not in vertex:
                    vertex.add(u)
                if v not in vertex:
                    vertex.add(v)




def main():
    a, b, c, d, e, f = range(6)
    g = {a: {b: 1, c: 2, d: 3, e: 6}, b: {a: 1, c: 2, e: 4}, c: {a: 2, b: 2, d: 2}, d: {a: 3, c: 2, f: 3},
         e: {a: 6, b: 4, f: 2}, f: {d: 3, e: 2}}
    seq = kruskal(g)
    print(seq)


if __name__ == '__main__':
    main()