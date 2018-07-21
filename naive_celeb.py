from random import randrange


# O(n^2)
def naive_celeb(g):
    """Everyone know celeb, but celeb don't know everyone"""
    n = len(g)
    for u in range(n):
        for v in range(n):
            if u == v: continue
            if g[u][v]: break
            if not g[v][u]: break
        else:
            return u
    return None


def main():
    n = 10
    g = [[randrange(2) for i in range(n)] for i in range(n)]
    c = randrange(n)
    for i in range(n):
        g[i][c] = True
        g[c][i] = False
    print(naive_celeb(g))


if __name__ == '__main__':
    main()