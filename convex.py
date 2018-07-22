# coding=utf-8


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


Mid = Point(0, 0)


def quad(point):
    """确定象限"""
    if point.x >= 0 and point.y >= 0:
        return 1
    elif point.x <= 0 and point.y >= 0:
        return 2
    elif point.x <= 0 and point.y <= 0:
        return 3
    elif point.x >= 0 and point.y <= 0:
        return 4


def partition(seq):
    pi, seq = seq[0], seq[1:]
    low = []
    high = []
    for i in seq:
        if compare(i, pi):
            low.append(i)
        else:
            high.append(i)
    return low, pi, high


def quick_sort(seq):
    if len(seq) <= 1: return seq
    low, pi, high = partition(seq)
    return quick_sort(low) + [pi] + quick_sort(high)


def compare(point_p, point_q):
    point1 = Point(point_p.x - Mid.x, point_p.y - Mid.y)
    point2 = Point(point_q.x - Mid.x, point_q.y - Mid.y)
    one = quad(point1)
    two = quad(point2)
    if one != two:
        return one < two
    return point1.x * point2.y > point2.x * point1.y


def orientation(point_a, point_b, point_c):
    """Checks whether the line is crossing the polygon"""
    res = (point_b.x - point_a.x) * (point_c.y - point_a.y) - \
          (point_c.x - point_a.x) * (point_b.y - point_a.y)
    if res == 0:
        return 0
    elif res > 0:
        return 1
    else:
        return -1


def merge(points_a, points_b):
    n1 = len(points_a)  # number of points in polygon a
    n2 = len(points_b)  # number of points in polygon b

    max_a = 0
    # find rightmost point of a
    for i in range(1, n1):
        if points_a[max_a].x < points_a[i].x:
            max_a = i

    max_b = 0
    # find leftmost point of b
    for i in range(1, n2):
        if points_b[max_b].x > points_b[i].x:
            max_b = i

    up_index_a = max_a
    up_index_b = max_b
    done = 1
    while done:
        # finding the upper tangent
        done = 0
        while orientation(points_a[up_index_a], points_b[up_index_b], points_b[(up_index_b - 1 + n2) % n2]) >= 0:
            up_index_b = (up_index_b - 1 + n2) % n2

        while orientation(points_b[up_index_b], points_a[up_index_a], points_a[(up_index_a + 1) % n1]) <= 0:
            up_index_a = (up_index_a + 1) % n1
            done = 1

    low_index_a = max_a
    low_index_b = max_b
    done = 1
    while done:
        # finding the lower tangent
        done = 0
        while orientation(points_a[low_index_a], points_b[low_index_b], points_b[(low_index_b + 1) % n2]) <= 0:
            low_index_b = (low_index_b + 1) % n2

        while orientation(points_b[low_index_b], points_a[low_index_a], points_a[(low_index_a - 1 + n1) % n1]) >= 0:
            low_index_a = (low_index_a - 1 + n1) % n1
            done = 1

    res = []
    res.append(points_a[up_index_a])
    while up_index_a != low_index_a:
        up_index_a = (up_index_a + 1) % n1
        res.append(points_a[up_index_a])
    res.append(points_b[up_index_b])
    while up_index_b != low_index_b:
        up_index_b = (up_index_b - 1 + n2) % n2
        res.append(points_b[up_index_b])
    return res


def brute(points):
    res = []
    s = set()
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1 = points[i].x
            y1 = points[i].y
            x2 = points[j].x
            y2 = points[j].y
            a1 = y1 - y2
            b1 = x2 - x1
            c1 = x1*y2 - x2*y1
            pos = 0
            neg = 0
            k = 0
            while k < len(points):
                if a1*points[k].x + b1*points[k].y + c1 >= 0:
                    pos += 1
                if a1*points[k].x + b1*points[k].y + c1 <= 0:
                    neg += 1
                if pos == len(points) or neg == len(points):
                    if i not in s:
                        s.add(i)
                        res.append(points[i])
                    if j not in s:
                        s.add(j)
                        res.append(points[j])
                k += 1
    global Mid
    Mid = Point(0, 0)
    for i in res:
        Mid.x += i.x
        Mid.y += i.y
        i.x *= len(res)
        i.y *= len(res)
    res = quick_sort(res)
    for i in res:
        i.x /= len(res)
        i.y /= len(res)
    return res


def divide(points):
    if len(points) <= 5:
        return brute(points)
    mid = len(points) // 2
    left = points[:mid]
    right = points[mid:]
    left = divide(left)
    right = divide(right)
    return merge(left, right)


def main():
    n = int(input())
    points = []
    for i in range(n):
        a, b = input().split()
        points.append(Point(float(a), float(b)))
    points.sort(key=lambda point: point.x)
    print("After sorted:")
    for i in points:
        print(i.x, i.y)
    points = divide(points)
    print("convex:")
    for i in points:
        print(i.x, i.y)


if __name__ == '__main__':
    main()