"""

Zig-zag 수열 게산하기

- 교재 p.111

https://www.youtube.com/watch?v=_967x3u8dKs

- 문제: 정수 n개의 수열이 A[0], ... , A[n-1]처럼 주어질 때, 이 수열에서 증가와 감소가 교대로 나타나는 zig-zag 수열 중 가장 긴 부분수열을 찾아, 그 길이를 출력하라.
- 1,7,4,9,2,5는 1에서 7로 증가, 7에서 4로 감소, 4에서 9로 증가 ... 증가와 감소가 교대로 나타나는 zig-zag 수열이다.
- 1,7,9,4,5,2는 처음에 두 번 증가를 하기 때문에 zig-zag 수열이 아니다.
- 4는 숫자 하나로 구성된 zig-zag 수열이다

Example:
>> zigzag([1,7,9,4,5,2])
5

"""


def zigzag(A):
    n = len(A)
    res = 0
    high, low = [1]*n, [1]*n
    for k in range(n):
        for j in range(k):
            if A[j] < A[k]:
                high[k] = max(high[k], low[j]+1)
            elif A[j] > A[k]:
                low[k] = max(low[k], high[j]+1)

    for k in range(n):
        res = max(high[k], low[k], res)
    return res


if __name__ == "__main__":
    A = list(int(x)
             for x in input("Enter numbers separated by a comma: ").strip().split(','))
    print(zigzag(A))
