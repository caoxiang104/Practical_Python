# O(n^2)
def naive_max_perm(m, a=None):
    """Find maximum permutation"""
    if a is None:
        a = set(range(len(m)))
    if len(a) == 1: return a
    b = set(m[i] for i in a)
    c = a - b
    if c:
        a.remove(c.pop())
        return naive_max_perm(m, a)
    return a


def main():
    seq = [2, 2, 0, 5, 3, 5, 7, 4]
    seq = naive_max_perm(seq)
    print("".join(str(seq)))


if __name__ == '__main__':
    main()