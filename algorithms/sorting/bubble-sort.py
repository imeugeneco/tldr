"""

Compare adjacent elements and swap if not in order

- Time complexity: O(n^2)
- Stable? Yes
- In-place? Yes

Examples:
>> bubble_sort([12,4,9,10,21,3,8,0,7,9,6])
0,3,4,6,7,8,9,9,10,12,21

>> bubble_sort([-29,4,0,-5,82])
-29,-5,0,4,82

"""


def bubble_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(1, n):
            if A[j-1] > A[j]:  # compare adjacent numbers
                A[j-1], A[j] = A[j], A[j-1]  # swap

    return A


if __name__ == "__main__":
    import doctest
    import time

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma: ").strip()
    unsorted = [int(n) for n in user_input.split(',')]
    start = time.process_time()
    print(*bubble_sort(unsorted), sep=",")
    print(f"Processing time: {(time.process_time()-start)%1e9 + 7}")
