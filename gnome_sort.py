# O(n^2)
def genome_sort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i - 1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i - 1] = seq[i - 1], seq[i]
            i -= 1


def main():
    seq = [1, 5, 3, 4, 6, 2]
    genome_sort(seq)
    print("".join(str(seq)))


if __name__ == '__main__':
    main()