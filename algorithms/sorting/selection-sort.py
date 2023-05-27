"""

Find the largest (or smallest) value and move it to a sorted list

- Time complexity: O(n^2)
- Stable? NO
- In-place? YES

Examples:
>> selection_sort([12,4,9,10,21,3,8,0,7,9,6])
0,3,4,6,7,8,9,9,10,12,21

"""


def selection_sort(A):
    n = len(A)
    for i in range(n-1, 0, -1):
        # get the index of the biggest number from A[0]~A[i]
        m = get_max_index(A, i)
        A[i], A[m] = A[m], A[i]  # swap
    return A


def get_max_index(A, i):
    m, m_index = A[0], 0
    for j in range(1, i+1):
        if m < A[j]:
            m, m_index = A[j], j
    return m_index


if __name__ == "__main__":
    import doctest
    import time

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma: ").strip()
    unsorted = [int(n) for n in user_input.split(',')]
    start = time.process_time()
    print(*selection_sort(unsorted), sep=",")
    print(f"Processing time: {(time.process_time()-start)%1e9 + 7}")
