# -*- coding:utf-8 -*-
"""
在一个地图上有n个地窖（n<=200）,每个地窖中埋有一定数量的地雷。同时，给出地窖之间的连接路径，
并规定路径都是单向的,且保证都是小序号地窖指向在序号地窖，也不存在可以从一个地窖出发经过若干
地窖后又回到原来地窖的路径。某人可以从任一处开始挖地雷，然后沿着指出的连接往下挖（仅能选择
一条路径），当无连接时挖地雷工作结束。设计一个挖地雷的方案，使他能挖到最多的地雷。
"""


def find_mine(num_mine, road, dp):
    n = len(num_mine)
    dp[n - 1] = num_mine[n - 1]
    for i in range(n-2, -1, -1):
        temp = 0
        for j in range(i + 1, n):
            if road[i][j] > 0:
                temp = max(temp, dp[j])
        dp[i] = num_mine[i] + temp
    return dp


def find_road(num_mine, dp):
    road = []
    max_mine = max(dp)
    index = dp.index(max_mine)
    max_mine -= num_mine[index]
    road.append(index+1)
    index += 1
    while index < len(num_mine) and max_mine > 0:
        if dp[index] == max_mine:
            road.append(index+1)
            max_mine -= num_mine[index]
        index += 1
    return road


def main():
    """输入地窖数:6
    输入每个地窖的雷数：5 10 20 5 4 5
    路径:1 2
    路径:1 4
    路径:3 4
    路径:4 5
    路径:4 6
    路径:5 6
    路径:0 0
    挖到地雷最大数： 19,10,34,14,9,5
    最大地雷数： 34
    路线图: 3->4->5->6"""
    n = int(input("输入地窖数:"))
    num_mine = input("输入每个地窖的雷数：")
    num_mine = list(map(int, num_mine.split()))
    road = [[0]*n for i in range(n)]  # 是否存在路径
    dp = [0]*n
    while 1:
        num1, num2 = input("路径:").split()
        num1, num2 = int(num1), int(num2)
        if num1 == 0 and num2 == 0:
            break
        else:
            road[num1-1][num2-1] = 1
    dp = find_mine(num_mine, road, dp)
    print("挖到地雷最大数：", ",".join(map(str, dp)))
    print("最大地雷数：", max(dp))
    print("路线图:", "->".join(map(str, find_road(num_mine, dp))))


if __name__ == '__main__':
    main()