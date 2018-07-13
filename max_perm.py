# O(n)
def max_perm(m):
    """Find maximum permutation"""
    n = len(m)
    a = set(range(n))
    count = [0]*n
    for i in m:
        count[i] += 1
    q = [i for i in a if count[i] == 0]
    while q:
        i = q.pop()
        a.remove(i)
        j = m[i]
        count[j] -= 1
        if count[j] == 0:
            q.append(j)
    return a


def main():
    seq = [2, 2, 0, 5, 3, 5, 7, 4]
    seq = max_perm(seq)
    print("".join(str(seq)))


if __name__ == '__main__':
    main()