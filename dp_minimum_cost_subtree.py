# -*- coding:utf-8 -*-
"""最小代价字母树"""
"""设有n堆沙子排成一排，其编号为1，2，3，…，n（n≤100）。每堆沙子有一定的数量，如下表 
13　7　8　16　21　4　18 现在要将n堆沙子归并成一堆
[输入格式] 
n {表示沙子的堆数, 2<=n<=100} 
a1 a2 … an {表示每堆沙子的数量,1<=Ai<=100} 
[输出格式] 
x {表示最小的归并总代价 } 
输入样例： 
7 
13 7 8 16 21 4 18 
输出样例： 
239"""


def min_num(num, dp, s):
    n = len(num)
    sum_ = 0
    for i in range(n):
        sum_ += num[i]
        s[i + 1] = sum_
        if i < n-1:
            dp[i + 1][i + 2] = num[i] + num[i + 1]
        dp[i + 1][i + 1] = 0
    for k in range(1, n):
        for i in range(1, n - k + 1):
            j = i + k
            min_ = float("Inf")
            for m in range(i, j):
                min_ = min(min_, dp[i][m] + dp[m+1][j])
            dp[i][j] = min_ + s[j] - s[i - 1]
    return dp[1][n]


def main():
    n = int(input("输入沙子的堆数:"))
    num = input("输入沙子的数量:")
    num = list(map(int, num.split()))
    dp = [[0]*(n+1) for i in range(n+1)]
    s = [0]*(n+1)
    print("最小归并代价为:", min_num(num, dp, s))
    for i in range(n + 1):
        print(dp[i])


if __name__ == '__main__':
    main()