# O(n^2)
def ins_sort_rec(seq, i):
    if i == 0: return
    ins_sort_rec(seq, i - 1)
    j = i
    while j > 0 and seq[j] < seq[j - 1]:
        seq[j], seq[j - 1] = seq[j - 1], seq[j]
        j -= 1


def main():
    seq = [1, 5, 3, 4, 6, 2]
    ins_sort_rec(seq, len(seq) - 1)
    print("".join(str(seq)))


if __name__ == '__main__':
    main()