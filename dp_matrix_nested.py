# -*- coding:utf-8 -*-
"""矩阵嵌套"""


# O(n log n)
def max_matrix(matrix, dp, min_in_max):
    for i in range(len(matrix)):
        if matrix[i][0] > matrix[i][1]:
            matrix[i][0], matrix[i][1] = matrix[i][1], matrix[i][0]
    matrix.sort(key=lambda x: x[0])
    dp[0] = 1
    min_in_max[0] = matrix[0][1]
    for i in range(1, len(matrix)):
        if matrix[i][1] >= min_in_max[dp[i - 1] - 1]:
            dp[i] = dp[i - 1] + 1
            min_in_max[dp[i] - 1] = matrix[i][1]
        else:
            dp[i] = dp[i - 1]
            low = 0
            high = dp[i] - 1
            mid = (low + high) // 2
            while low <= high:
                if matrix[i][1] >= min_in_max[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
                mid = (low + high) // 2
            min_in_max[low] = matrix[i][1]
    return dp[len(matrix) - 1]


def main():
    n = int(input("输入矩阵长度:"))
    matrix = []
    for i in range(n):
        x, y = input().split()
        matrix.append([int(x), int(y)])
    dp = [0]*len(matrix)
    min_in_max = [0]*len(matrix)
    print("最长嵌套矩阵（包含矩阵相等的情况）的个数为：", max_matrix(matrix, dp, min_in_max))


if __name__ == '__main__':
    main()