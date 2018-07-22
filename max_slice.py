# o(nlog(n))
def find_max_cross_subarray(array, low, mid, high):
    left_sum = array[mid]
    Sum = array[mid]
    left_index = mid
    for i in range(mid-1, low-1, -1):
        Sum += array[i]
        if Sum > left_sum:
            left_sum = Sum
            left_index = i
    right_sum = 0
    Sum = 0
    right_index = mid
    for i in range(mid+1, high+1):
        Sum += array[i]
        if Sum > right_sum:
            right_sum = Sum
            right_index = i
    max_sum = left_sum + right_sum
    return [left_index, right_index, max_sum]


def find_max_subarray(A, low, high):
    if low == high:
        return [low, high, A[low]]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_max_subarray(A, low, mid)
        right_low, right_high, right_sum = find_max_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_cross_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return [left_low, left_high, left_sum]
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return [right_low, right_high, right_sum]
        elif cross_sum >= left_sum and cross_sum >= right_sum:
            return [cross_low, cross_high, cross_sum]


def main():
    seq = [-1, 2, 0, -5, 3, 5, -7, 4]
    index1, index2, seq = find_max_subarray(seq, 0, len(seq) - 1)
    print(index1, index2)
    print("".join(str(seq)))


if __name__ == '__main__':
    main()