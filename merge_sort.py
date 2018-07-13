# O(n log(n))
def merge_sort(seq):
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1:
        merge_sort(lft)
    if len(rgt) > 1:
        merge_sort(rgt)
    i = 0
    j = 0
    k = 0
    while i < len(lft) and j < len(rgt):
        if lft[i] >= rgt[j]:
            seq[k] = rgt[j]
            k += 1
            j += 1
        else:
            seq[k] = lft[i]
            k += 1
            i += 1
    while i < len(lft):
        seq[k] = lft[i]
        k += 1
        i += 1
    while j < len(rgt):
        seq[k] = rgt[j]
        k += 1
        j += 1
    return seq


def main():
    seq = [1, 5, 3, 4, 6, 2]
    seq = merge_sort(seq)
    print("".join(str(seq)))


if __name__ == '__main__':
    main()
