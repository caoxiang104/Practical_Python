import sys


class Point(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)


def main():
    n = 10
    points = []
    for i in range(n):
        a, b = input().split()
        points.append(Point(a, b))
    points.sort()
    for i in points:
        print(i.x, i.y)


if __name__ == '__main__':
    main()