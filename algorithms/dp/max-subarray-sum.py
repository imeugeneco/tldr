"""

연속구간의 최대 합 구하기 연습문제

Problem: Given an array A of n integers, what is the largest sum of any nonempty subarray?
https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/487dc976eabd0f9bcd6a3c385203ea27_MIT6_006S20_r16.pdf

Examples:
>> find_max_sum_range([-5, 4, 1, -4, 5], 5)
6

"""


def solution(A, n):
    S = [0]*n
    S[0] = A[0]
    for i in range(1, n):
        S[i] = max(S[i-1]+A[i], A[i])
    return max(S)


if __name__ == "__main__":
    import doctest
    import time

    doctest.testmod()

    nums = list(int(x)
                for x in input("Enter numbers separated by a comma: ").strip().split(','))
    start = time.process_time()
    print(solution(nums, len(nums)))
    print(f"Processing time: {(time.process_time()-start)%1e9 + 7}")
