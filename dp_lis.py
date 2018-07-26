# -*- coding:utf-8 -*-
# 最长单调递增子序列


# O(n^2)
def lis_len(seq_a, seq_b, dp, flag):
    """将序列X按非递减顺序排列，形成新序列Y，问题就转变成求解X和Y的LCS"""
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


# O(n^2)
def lis_len2(seq_a, dp2):
    """设d[i]为以第i个元素结尾的最长递增子序列的长度，
    则d[i]=max{0,d[j] | j<i,a[j]<a[i]}+1,ans=max{d[i]}."""
    len_a = len(seq_a)
    dp2[0] = 1
    for i in range(1, len_a):
        temp_max = 0
        for j in range(i):
            if seq_a[i] >= seq_a[j]:
                temp_max = max(temp_max, dp2[j])
        dp2[i] = temp_max + 1
    return max(dp2)


# O(n log n)
def lis_len3(seq_a, dp3, min_in_max):
    """ 假设 result数组保存以X[i]结尾的最长递增子序列的长度，X的LIS的长度为K。
    由于长度为i（ 1 <= i <= k )的LIS可能不止一个，那么我们用数组minInMax记录
    下长度相同的LIS的末尾元素中的最小值。如果X[i] 大于 minInMax[ result[i-1] ] ,
    那么result[i] = result[i-1] +1,否则，result[i]与result[i-1]相等。由于
    minInMax是递增的，所以使用二分查找确定array[i]应该放在哪个位置上"""
    len_a = len(seq_a)
    dp3[0] = 1
    min_in_max[0] = seq_a[0]
    for i in range(1, len_a):
        if seq_a[i] >= min_in_max[dp3[i - 1]]:
            dp3[i] = dp3[i - 1] + 1
            min_in_max[dp3[i]] = seq_a[i]
        else:
            dp3[i] = dp3[i - 1]
            low = 0
            high = dp3[i - 1] - 1
            mid = (low + high) // 2
            while low <= high:
                if seq_a[i] <= min_in_max[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
                mid = (low + high) // 2
            min_in_max[low + 1] = seq_a[i]
    return dp3[len(seq_a) - 1]


def print_lis2(seq, dp2):
    max_dp = max(dp2)
    out = []
    i = len(seq) - 1
    while max_dp:
        if dp2[i] == max_dp:
            out.append(seq[i])
            max_dp -= 1
        i -= 1
    return out


def print_lis(seq_a, len_a, len_b, flag, lcs):
    if len_a == 0 or len_b == 0:
        return lcs
    if flag[len_a][len_b] == 0:
        return lcs
    elif flag[len_a][len_b] == 1:
        lcs.append(seq_a[len_a - 1])  # 序列比flag长度小一
        return print_lis(seq_a, len_a - 1, len_b - 1, flag, lcs)
    elif flag[len_a][len_b] == 2:
        return print_lis(seq_a, len_a - 1, len_b, flag, lcs)
    else:
        return print_lis(seq_a, len_a, len_b - 1, flag, lcs)


def main():
    a = input("输入序列a:")
    seq_a = list(map(int, a.split()))
    seq_b = sorted(seq_a)
    len_a = len(seq_a)
    len_b = len(seq_b)
    dp = [[0]*(len_a + 1) for i in range(len_a + 1)]
    dp2 = [0]*len_a
    dp3 = [0]*len_a
    min_in_max = [0] * len_a
    flag = [[0]*(len_a + 1) for i in range(len_a + 1)]
    print("序列长度为：", lis_len(seq_a, seq_b, dp, flag))
    lcs = []
    print("序列为：", print_lis(seq_a, len_a, len_b, flag, lcs)[::-1])
    print("法二序列长度为：", lis_len2(seq_a, dp2))
    print("法二序列为：", print_lis2(seq_a, dp2)[::-1])
    print("法三序列长度为：", lis_len3(seq_a, dp3, min_in_max))


if __name__ == '__main__':
    main()