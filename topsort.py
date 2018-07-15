def topsort(g):
    count = dict((u, 0) for u in range(len(g)))
    for u in g:
        for v in u:
            count[v] += 1
    c = []
    q = [u for u in range(len(g)) if count[u] == 0]
    while q:
        u = q.pop()
        c.append(u)
        for v in g[u]:
            count[v] -= 1
            if count[v] == 0:
                q.append(v)
    return c


def main():
    a, b, c, d, e = range(5)
    g = [[c, e], [], [b, e], [b], [d]]
    seq = topsort(g)
    print(seq)


if __name__ == '__main__':
    main()