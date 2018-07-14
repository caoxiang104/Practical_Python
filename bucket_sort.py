# O(n)
from math import floor


def bucket_sort(a, n):
    c = [[] for i in range(n)]
    b = []
    for i in a:
        c[int(floor(n * i))].append(i)
    for i in range(len(c)):
        ins_sort(c[i])
    for i in c:
        b.extend(i)
    return b


def ins_sort(a):
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1


def main():
    a = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    a = bucket_sort(a, 10)
    print("after bucket sort:", a)


if __name__ == '__main__':
    main()