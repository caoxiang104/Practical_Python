def knapsack(w, v, N, c):
    for j in range(1, c + 1):
        for i in range(1, len(w)):
            if j >= w[i]:
                N[i][j] = max(N[i - 1][j], N[i - 1][j-w[i]] + v[i])
            else:
                N[i][j] = N[i - 1][j]
    return N


def traceback(N, w, c):
    out = [0] * len(N)
    for i in range(len(N) - 1, 0, -1):
        if N[i][c] == N[i - 1][c]:
            out[i] = 0
        else:
            out[i] = 1
            c -= w[i]
    return out


def main():
    w = [0, 15, 10, 12, 8]
    v = [0, 12, 8, 9, 5]
    c = 30
    N = [[0]*(c+1) for i in range(len(w))]
    N = knapsack(w, v, N, c)
    out = traceback(N, w, c)
    print(N[len(w) - 1][c])
    print(out)


if __name__ == '__main__':
    main()