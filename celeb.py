from random import randrange


# O(n)
def celeb(g):
    """Everyone know celeb, but celeb don't know everyone"""
    n = len(g)
    u, v = 0, 1
    for c in range(2, n+1):
        if g[u][v]:
            u = c
        else:
            v = c
    if u == n:
        c = v
    else:
        c = u
    for v in range(n):
        if c == v: continue
        if g[c][v]: break
        if not g[v][c]: break
    else:
        return c
    return None


def main():
    n = 10
    g = [[randrange(2) for i in range(n)] for i in range(n)]
    c = randrange(n)
    for i in range(n):
        g[i][c] = True
        g[c][i] = False
    print(celeb(g))


if __name__ == '__main__':
    main()