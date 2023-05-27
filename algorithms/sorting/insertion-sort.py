"""

Gradually align from the left (or right)

- Time complexity: O(n^2)
- Stable? Yes
- In-place? Yes

Examples:
>> insertion_sort([19,2,31,45,30,11,121,27])
2,11,19,27,30,31,45,121

"""


def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        j = i - 1
        while j >= 0 and A[j] > A[j+1]:  # compare current element with the next
            A[j], A[j+1] = A[j+1], A[j]
            j = j-1
    return A


if __name__ == "__main__":
    import doctest
    import time

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma: ").strip()
    unsorted = [int(n) for n in user_input.split(',')]
    start = time.process_time()
    print(*insertion_sort(unsorted), sep=",")
    print(f"Processing time: {(time.process_time()-start)%1e9 + 7}")
