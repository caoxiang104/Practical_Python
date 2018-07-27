# -*- coding:utf-8 -*-
"""
给出一个1到n的排列，每次可以移动一个数到一个任意位置。问要达到状态1,2,3……n至少移动多少次？
即求最大递增子序列，结果为长度减去最大递增子序列
Sample Input
5
2 1 4 5 3
Sample Output
2
"""


def min_move_times(num, dp, min_in_max):
    n = len(num)
    dp[0] = 1
    min_in_max[0] = num[0]
    for i in range(1, n):
        if num[i] > min_in_max[dp[i - 1] - 1]:
            dp[i] = dp[i - 1] + 1
            min_in_max[dp[i] - 1] = num[i]
        else:
            dp[i] = dp[i - 1]
            low = 0
            high = dp[i] - 1
            mid = (low + high) // 2
            while low <= high:
                if num[i] >= min_in_max[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
                mid = (low + high) // 2
            min_in_max[low] = num[i]
    return dp[n - 1]


def main():
    n = int(input("请输入长度："))
    num = input("请输入数字序列：")
    num = list(map(int, num.split()))
    dp = [0]*n
    min_in_max = [0]*n
    print("最小移动次数：", n-min_move_times(num, dp, min_in_max))


if __name__ == "__main__":
    main()