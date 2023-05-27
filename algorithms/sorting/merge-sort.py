"""

Divide into equal halves and merge in a sorted manner

- Time complexity: O(nlogn)
- Stable? YES
- In-place? NO

Examples:
>> merge_sort([1,3,5,7,9,2,4,6,8,10])
1,2,3,4,5,6,7,8,9,10

"""


def merge_sort(A):
    n = len(A)
    if n <= 1:
        return A
    middle = n//2  # find mid point and divide array into equal halves
    left = A[:middle]
    right = A[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return list(merge(left, right))


def merge(left, right):
    B = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            B.append(left.pop(0))
        else:
            B.append(right.pop(0))
    if len(left) == 0:
        B = B+right
    else:
        B = B + left
    return B


if __name__ == "__main__":
    import doctest
    import time

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma: ").strip()
    unsorted = [int(n) for n in user_input.split(',')]
    start = time.process_time()
    print(*merge_sort(unsorted), sep=",")
    print(f"Processing time: {(time.process_time()-start)%1e9 + 7}")
