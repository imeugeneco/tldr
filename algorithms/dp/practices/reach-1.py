"""

[백준] 1로 만들기
https://www.acmicpc.net/problem/1463

- 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
    1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
    2. X가 2로 나누어 떨어지면, 2로 나눈다.
    3. 1을 뺀다.
- 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

- 입력: 첫째 줄에 1보다 크거나 같고, 10^6보다 작거나 같은 정수 N이 주어진다.
- 출력: 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

예시:
>> 2
출력: 1

>> 10
출력: 3

"""


def sol(n):
    if n <= 2:
        return n-1

    dp = [0]*(n+1)
    dp[2], dp[3] = 1, 1

    for i in range(3, n+1):
        if i % 6 == 0:
            dp[i] = min(dp[i//3], dp[i//2], dp[i-1])+1
        elif i % 3 == 0:
            dp[i] = min(dp[i//3], dp[i-1]) + 1
        elif i % 2 == 0:
            dp[i] = min(dp[i//2], dp[i-1]) + 1
        else:
            dp[i] = dp[i-1]+1
    return dp[n]


if __name__ == "__main__":
    n = int(input())
    print(sol(n))
