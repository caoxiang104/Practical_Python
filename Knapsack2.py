# -*- coding:utf-8 -*-
"""完全背包表示每个物品可以取无限次，只要加起来总容量不超过V就可以。
同样可以用f[i][j]表示前i间物品恰放入一个容器为j的背包可以获得的最大价值。则其状态转移方程为：
f[i][j] = max{f[i-1][j-k*weight[i]]+k*value[i]} ,其中(0<=k<=j/weight[i]) """


def knapsack(w, v, N, c):
    for j in range(1, c + 1):
        for i in range(1, len(w)):
            N[i][j] = N[i - 1][j]
            for k in range(1, j//w[i] + 1):
                N[i][j] = max(N[i][j], N[i - 1][j-k*w[i]] + k*v[i])
    return N


def traceback(N, w, v, c):
    out = [0] * len(N)
    for i in range(len(N) - 1, 0, -1):
        if N[i][c] == N[i - 1][c]:
            out[i] = 0
        else:
            for k in range(1, c // w[i] + 1):
                if N[i][c] == N[i - 1][c - k*w[i]] + k*v[i]:
                    out[i] = k
                    c = c - k*w[i]
    return out


def main():
    w = [0, 15, 10, 12, 8]
    v = [0, 12, 8, 9, 5]
    c = 42
    N = [[0]*(c+1) for i in range(len(w))]
    N = knapsack(w, v, N, c)
    out = traceback(N, w, v, c)
    print(N[len(w) - 1][c])
    print(out)
    for i in range(len(N)):
        print(N[i])


if __name__ == '__main__':
    main()