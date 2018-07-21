from math import sqrt


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return repr((self.x, self.y))


def distance(point1, point2):
    return sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)


def min_point_pair_2d(points, low, high):
    if high == low + 1:
        return points[low], points[high], distance(points[low], points[high])
    elif high == low + 2:
        dis1 = distance(points[low], points[low + 1])
        dis2 = distance(points[low], points[low + 2])
        dis3 = distance(points[low + 1], points[low + 2])
        if dis1 <= dis2 and dis1 <= dis3:
            return points[low], points[low + 1], dis1
        elif dis2 <= dis3 and dis2 <= dis1:
            return points[low], points[low + 2], dis2
        elif dis3 <= dis1 and dis3 <= dis2:
            return points[low + 1], points[low + 2], dis3
    else:
        mid = (high + low) // 2
        left_po1, left_po2, left_dis = min_point_pair_2d(points, low, mid)
        right_po1, right_po2, right_dis = min_point_pair_2d(points, mid + 1, high)
        if left_dis <= right_dis:
            pos1 = left_po1
            pos2 = left_po2
            dis = left_dis
        else:
            pos1 = right_po1
            pos2 = right_po2
            dis = right_dis
        points_temp = []
        for i in range(mid, low - 1, -1):
            if points[mid].x - points[i].x <= dis:
                points_temp.append(points[i])
        for i in range(mid + 1, high + 1):
            if points[i].x - points[mid].x <= dis:
                points_temp.append(points[i])
        points_temp.sort(key=lambda point: point.y)
        for i in range(len(points_temp)):
            for j in range(i + 1, len(points_temp)):
                if points_temp[j].y - points_temp[i].y > dis:
                    break
                elif points_temp[i].x <= mid and points_temp[j].x <= mid:
                    continue
                elif points_temp[i].x > mid and points_temp[j].x > mid:
                    continue
                else:
                    cross_dis = distance(points_temp[i], points_temp[j])
                    if cross_dis < dis:
                        pos1 = points_temp[i]
                        pos2 = points_temp[j]
                        dis = cross_dis
        return pos1, pos2, dis


def main():
    n = 10
    points = []
    for i in range(n):
        a, b = input().split()
        points.append(Point(float(a), float(b)))
    points.sort(key=lambda point: point.x)
    pos1, pos2, dis = min_point_pair_2d(points, 0, len(points) - 1)
    print(pos1.x, pos1.y)
    print(pos2.x, pos2.y)
    print(dis)


if __name__ == '__main__':
    main()

