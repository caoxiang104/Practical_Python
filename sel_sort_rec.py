# O(n^2)
def sel_sort_rec(seq, i):
    if i == 0: return
    max_j = i
    for j in range(i):
        if seq[j] > seq[max_j]:
            max_j = j
        seq[i], seq[max_j] = seq[max_j], seq[i]
    sel_sort_rec(seq, i - 1)


def main():
    seq = [1, 5, 3, 4, 6, 2]
    sel_sort_rec(seq, len(seq) - 1)
    print("".join(str(seq)))


if __name__ == '__main__':
    main()