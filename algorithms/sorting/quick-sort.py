"""

Select a pivot value, divide-and-conquer sublists of smaller/equal/larger elements, merge sublists.

- Performance can vary greatly depending on the pivot value. 
- Ideally, the same number of small and large values are divided into equal halves, resulting in a time complexity of O(nlogn).
- Worst-case time complexity can be O(n^2) if the values are skewed on one side.

- Time complexity: O(nlogn)

Examples:
>> quick_sort([4,2,5 8 6,2,3,7,10])
2,2,3,4,5,6,7,8,10

"""


def quick_sort(A):
    n = len(A)
    if n <= 1:
        return A
    pivot = A[0]
    S, M, L = [], [], []
    for x in A:
        if x < pivot:
            S.append(x)
        elif x > pivot:
            L.append(x)
        else:
            M.append(x)
    return quick_sort(S) + M + quick_sort(L)


if __name__ == "__main__":
    import doctest
    import time

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma: ").strip()
    unsorted = [int(n) for n in user_input.split(',')]
    start = time.process_time()
    print(*quick_sort(unsorted), sep=",")
    print(f"Processing time: {(time.process_time()-start)%1e9 + 7}")
