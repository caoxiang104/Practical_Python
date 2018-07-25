# -*- coding:utf-8 -*-
"""多重背包是每个物品有不同的个数限制，如第i个物品个数为num[i]。
同样可以用f[i][j]表示前i间物品恰放入一个容器为j的背包可以获得的最大价值，且每个物品数量不超多num[i]。则其状态转移方程为：
f[i][j] = max{f[i-1][j-k*weight[i]]+k*value[i]} ,其中(0<=k<=min{j/weight[i], num[i]})"""


def knapsack(w, v, N, c, num):
    for j in range(1, c + 1):
        for i in range(1, len(w)):
            N[i][j] = N[i - 1][j]
            max_num = min(num[i], j//w[i])
            for k in range(1, max_num + 1):
                N[i][j] = max(N[i][j], N[i - 1][j-k*w[i]] + k*v[i])
    return N


def traceback(N, w, v, c, num):
    out = [0] * len(N)
    for i in range(len(N) - 1, 0, -1):
        if N[i][c] == N[i - 1][c]:
            out[i] = 0
        else:
            max_num = min(num[i], c // w[i])
            for k in range(1,  max_num + 1):
                if N[i][c] == N[i - 1][c - k*w[i]] + k*v[i]:
                    out[i] = k
                    c = c - k*w[i]
    return out


def main():
    w = [0, 15, 10, 12, 8]
    v = [0, 12, 8, 9, 5]
    num = [0, 1, 4, 5, 3]
    c = 42
    N = [[0]*(c+1) for i in range(len(w))]
    N = knapsack(w, v, N, c, num)
    out = traceback(N, w, v, c, num)
    print(N[len(w) - 1][c])
    print(out)
    for i in range(len(N)):
        print(N[i])


if __name__ == '__main__':
    main()