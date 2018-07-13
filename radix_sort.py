# O(dn)
from collections import defaultdict


def counting_sort(a, time, key=lambda x: x):
    b, c = [], defaultdict(list)
    for x in a:
        c[key(x) // time % 10].append(x)
    for k in range(min(c), max(c) + 1):
        b.extend(c[k])
    return b


def radix_sort(a):
    n = len(str(max(a)))
    temp = 10
    for i in range(n):
        a = counting_sort(a, temp ** i)
    return a


def main():
    seq = [301, 425, 232, 426, 520, 1000, 20]
    seq = radix_sort(seq)
    print("".join(str(seq)))


if __name__ == '__main__':
    main()


