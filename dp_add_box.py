# -*- coding:utf-8 -*-
"""
某港口有一批箱子，将其编号，分别为1至N。每一个箱子的尺寸规格是一样的，现在要将其中某些箱子叠放起来，箱子叠放的规则如下：
一、每个箱子上最多只能直接叠放一个箱子；
二、编号较小的箱子不能放在编号较大的箱子之上；
三、每个箱子都给出了自身重量与可承受重量，每个箱子之上的所有箱子重量之和不得超过该箱的可承受重量。
为了节约堆放场地，希望你编程从中选出最多个箱子，使之能够在满足条件的情况下叠放起来。
【输入】
第一行是一个整数N（1≤N≤1000）。
以下共有N行，每行两个整数，中间以空格分隔，分别表示每个箱子的自身重量与可承受重量，两个数值均为小于等于3000的正整数。
【输出】
第一行应当输出最多可叠放的箱子总数M。
【样例】有五个箱子，如下表：
1 19 15
2 7 13
3 5 7
4 6 8
5 1 2
则最多可以叠放4个箱子，方案之一如：1、2、3、5
"""


def max_box(box, dp):
    n = len(box)
    dp[0] = 1
    min_in_max = []
    weight = list(map(lambda x: x[0], box))
    capacity = list(map(lambda x: x[1], box))
    min_in_max.append(capacity[0])
    i = 1
    while i < len(weight):
        min_num = min(min_in_max)
        if weight[i] <= min_num:
            dp[i] = dp[i - 1] + 1
            min_in_max = [j - weight[i] for j in min_in_max]
            min_in_max.append(capacity[i])
            i += 1
        else:
            dp[i] = dp[i - 1]
            min_index = min_in_max.index(min_num)
            temp = [j for j in min_in_max]
            temp.pop(min_index)
            temp = [j - weight[i] for j in temp]
            for j in range(min_index):
                temp[j] += weight[min_index]
            weight.pop(min_index)
            capacity.pop(min_index)
            if min(temp) > min_num:
                min_in_max = temp
                min_in_max.append(capacity[i])
    return dp[i - 1]


def main():
    n = int(input("请输入箱子总数："))
    box = []
    for i in range(n):
        num, weight, capacity = input("箱子：").split()
        box.append([int(weight), int(capacity)])
    dp = [0]*n
    print("箱子数量：", max_box(box, dp))


if __name__ == '__main__':
    main()