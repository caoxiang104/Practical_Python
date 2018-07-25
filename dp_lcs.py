# -*- coding:utf-8 -*-
"""最大公共子序列"""


def lcs_len(seq_a, seq_b, dp, flag):
    len_a = len(seq_a)
    len_b = len(seq_b)
    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            if seq_a[i - 1] == seq_b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                flag[i][j] = 1   # 斜上角
            elif dp[i - 1][j] > dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j]
                flag[i][j] = 2   # 上方
            else:
                dp[i][j] = dp[i][j - 1]
                flag[i][j] = 3  # 左方
    return dp[len_a][len_b]


def print_lcs(seq_a, len_a, len_b, flag, lcs):
    if len_a == 0 or len_b == 0:
        return lcs
    if flag[len_a][len_b] == 0:
        return lcs
    elif flag[len_a][len_b] == 1:
        lcs.append(seq_a[len_a - 1])  # 序列比flag长度小一
        return print_lcs(seq_a, len_a - 1, len_b - 1, flag, lcs)
    elif flag[len_a][len_b] == 2:
        return print_lcs(seq_a, len_a - 1, len_b, flag, lcs)
    else:
        return print_lcs(seq_a, len_a, len_b - 1, flag, lcs)


def main():
    a = input("输入序列a:")
    b = input("输入序列b:")
    seq_a = list(map(int, a.split()))
    seq_b = list(map(int, b.split()))
    len_a = len(seq_a)
    len_b = len(seq_b)
    dp = [[0]*(len_a + 1) for i in range(len_b + 1)]
    flag = [[0]*(len_a + 1) for i in range(len_b + 1)]
    print("序列长度为：", lcs_len(seq_a, seq_b, dp, flag))
    lcs = []
    print("序列为：", print_lcs(seq_a, len_a, len_b, flag, lcs)[::-1])


if __name__ == '__main__':
    main()