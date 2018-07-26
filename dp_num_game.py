# -*- coding:utf-8 -*-
"""                数字游戏
让a[i]和b[i]，关于b降序排列。减少得多的先被擦掉，就可以让剩下的和尽可能的大
dp[i][j]表示前i个数字在第j轮的时候的最大取值
dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+a[i]-b[i]*(j-1))"""


# O(n log n)
def max_num(a, b, m, dp):
    temp = []
    for i in range(len(a)):
        temp.append([a[i], b[i]])
    temp.sort(key=lambda x: x[1], reverse=True)
    a = list(map(lambda x: x[0], temp))
    b = list(map(lambda x: x[1], temp))
    for i in range(1, len(a) + 1):
        for j in range(1, m+1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + a[i - 1] - b[i - 1]*(j - 1))
    return dp[len(a)][m]


def main():
    """输入原序列:10 20 30
    输入下降数值:4 5 6
    输入轮数:3
    输出最大值为: 47"""
    a = input("输入原序列:")
    b = input("输入下降数值:")
    m = int(input("输入轮数:"))
    a = list(map(int, a.split()))
    b = list(map(int, b.split()))
    dp = [[0]*(len(a) + 1) for i in range(m + 1)]
    print("最大值为:", max_num(a, b, m, dp))


if __name__ == '__main__':
    main()