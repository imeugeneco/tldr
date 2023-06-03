"""

[백준] 피보나치 수 1
https://www.acmicpc.net/problem/24416

재귀호출에 비해 동적 프로그래밍이 얼마나 빠른지 확인해 보자. 
재귀 (fibo_rec)와 동적계획법(fibo_dp)으로 n의 피보나치 수를 구할 경우 각 알고리즘의 실행 횟수를 출력하자.

- 첫째 줄에 n(5 ≤ n ≤ 40)이 주어진다.
- fibo_rec fibo_dp 실행 횟수를 한 줄에 출력한다.

Examples
>> compare_fibo(5)
5 3

>> compare_fibo(30)
832040 28

"""


def fibo_rec(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)


def fibo_dp(n):
    dp = [0] * (n+1)
    dp[1] = dp[2] = 1
    count = 0
    for i in range(3, n+1):
        count += 1
        dp[i] = dp[i-1]+dp[i-2]
    return count


if __name__ == "__main__":
    n = int(input())
    count_rec = fibo_rec(n)
    count_dp = fibo_dp(n)
    print(count_rec, count_dp)
