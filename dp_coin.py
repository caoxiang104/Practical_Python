# -*- coding:utf-8 -*-
# def find_index(coin_num, s, low, high):
#     if low == high:
#         return low
#     elif low + 1 == high:
#         if s < coin_num[low]:
#             return low - 1
#         elif coin_num[high] > s >= coin_num[low]:
#             return low
#         else:
#             return high
#     else:
#         mid = (low + high) // 2
#         if coin_num[mid] == s:
#             return mid
#         elif coin_num[mid] > s:
#             return find_index(coin_num, s, low, mid - 1)
#         else:
#             return find_index(coin_num, s, mid + 1, high)


def coin(coin_num, s, dp):
    min_coin = min(coin_num)
    max_coin = max(coin_num)
    if s < min_coin:
        return dp
    for i in range(min_coin, s+1):
        if i < max_coin:
            dp[i] = dp[i - coin_num[0]] + 1
            for k in range(1, len(coin_num)):
                if i >= coin_num[k]:
                    dp[i] = min(dp[i], dp[i - coin_num[k]] + 1)
        else:
            dp[i] = dp[i - coin_num[0]] + 1
            for k in range(1, len(coin_num)):
                dp[i] = min(dp[i], dp[i - coin_num[k]] + 1)
    return dp


def find_coin(coin_num, dp, s):
    co = []
    while s:
        for j in range(len(coin_num)):
            if dp[s] == dp[s - coin_num[j]] + 1:
                co.append(coin_num[j])
                s -= coin_num[j]
                break
    return co


def main():
    coin_num = input()
    coin_num = list(map(int, coin_num.split()))  # 币种
    s = int(input())  # 钱数
    num = [0 for i in range(s + 1)]
    dp = coin(coin_num, s, num)
    print(dp[s])
    print(find_coin(coin_num, dp, s))


if __name__ == '__main__':
    main()