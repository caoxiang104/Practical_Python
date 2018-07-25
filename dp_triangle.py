from random import randint


def triangle(num):
    dp = num
    for i in range(len(num)-2, -1, -1):
        for j in range(0, i+1):
            dp[i][j] = dp[i][j] + max(dp[i+1][j], dp[i+1][j+1])
    return dp


def main():
    n = int(input())
    nums = [[-1]*n for i in range(n)]
    for i in range(len(nums)):
        for j in range(i+1):
            nums[i][j] = randint(1, n)
    for i in range(len(nums)):
        print(nums[i])
    dp = triangle(nums)
    for i in range(len(dp)):
        print(dp[i])
    print("max_sum:", dp[0][0])


if __name__ == '__main__':
    main()