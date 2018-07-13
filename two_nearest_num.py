from random import randrange
# method 1 O(n**2)
def twoNearestNum1(seq):
    dd = float("Inf")
    for i in seq:
        for j in seq:
            if i == j:
                continue
            d = abs(i - j)
            if d < dd:
                ii, jj, dd = i, j, d
    return ii, jj, dd


# method 2 O(n*log(n))
def twoNearestNum2(seq):
    dd = float("Inf")
    seq.sort()
    for i in range(len(seq) - 1):
        x, y = seq[i], seq[i + 1]
        if x == y:
            continue
        d = abs(x - y)
        if d < dd:
            xx, yy, dd = x, y, d
    return xx, yy, dd


def main():
    seq = [randrange(10 ** 10) for i in range(100)]
    xx, yy, dd = twoNearestNum1(seq)
    print(xx, yy, dd)
    xx, yy, dd = twoNearestNum2(seq)
    print(xx, yy, dd)


if __name__ == "__main__":
    main()