# o(n)
from collections import defaultdict


def counting_sort(a, key=lambda x: x):
    b, c = [], defaultdict(list)
    for x in a:
        c[key(x)].append(x)
    for k in range(min(c), max(c) + 1):
        b.extend(c[k])
    return b


def main():
    seq = [1, 5, 3, 4, 5, 1000, 2]
    seq = counting_sort(seq)
    print("".join(str(seq)))


if __name__ == '__main__':
    main()