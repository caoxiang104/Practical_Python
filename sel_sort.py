# O(n^2)
def sel_sort(seq):
    for i in range(len(seq) - 1, -1, -1):
        max_j = i
        for j in range(i):
            if seq[j] > seq[max_j]:
                max_j = j
        seq[max_j], seq[i] = seq[i], seq[max_j]


def main():
    seq = [1, 5, 3, 4, 6, 2]
    sel_sort(seq)
    print("".join(str(seq)))


if __name__ == '__main__':
    main()