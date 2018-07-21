def min_cross_point_pair(seq, mid):
    return [mid - 1, mid, abs(seq[mid] - seq[mid - 1])]


def min_point_pair(seq, low, high):
    if low == high - 1:
        return [low, high, abs(seq[high] - seq[low])]
    elif low == high:
        return [low, high, float("Inf")]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_len = min_point_pair(seq, low, mid)
        cross_low, cross_high, cross_len = min_cross_point_pair(seq, mid)
        right_low, right_high, right_len = min_point_pair(seq, mid, high)
        if left_len <= right_len and left_len <= cross_len:
            return [left_low, left_high, left_len]
        elif right_len <= cross_len and right_len <= left_len:
            return [right_low, right_high, right_len]
        elif cross_len <= left_len and cross_len <= right_len:
            return [cross_low, cross_high, cross_len]


def main():
    a = [2, 20, 200, 500, 499, 40, 10, 50]
    print(min_point_pair(a, 0, len(a) - 1))


if __name__ == '__main__':
    main()