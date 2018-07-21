from random import shuffle


def partition(seq):
    pi, seq = seq[0], seq[1:]
    low = [x for x in seq if x <= pi]
    high = [x for x in seq if x > pi]
    return low, pi, high


def quick_sort(seq):
    if len(seq) <= 1: return seq
    low, pi, high = partition(seq)
    return quick_sort(low) + [pi] + quick_sort(high)


def main():
    a = [i for i in range(12)]
    shuffle(a)
    print(quick_sort(a))


if __name__ == '__main__':
    main()