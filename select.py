from random import shuffle


def partition(seq):
    pi, seq = seq[0], seq[1:]
    low = [x for x in seq if x <= pi]
    high = [x for x in seq if x > pi]
    return low, pi, high


def select(seq, k):
    low, pi, high = partition(seq)
    m = len(low)
    if m == k: return pi
    elif m < k:
        return select(high, k-m-1)
    else:
        return select(low, k)


def main():
    a = [i for i in range(10)]
    shuffle(a)
    print(select(a, 5))


if __name__ == '__main__':
    main()