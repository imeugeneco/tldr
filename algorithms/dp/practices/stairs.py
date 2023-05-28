"""

[백준] 계단 오르기
https://www.acmicpc.net/problem/2579

- 계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다. 각각의 계단에는 일정한 점수가 쓰여 있는데 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.
- 계단 오르는 데는 다음과 같은 규칙이 있다.
    1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
    2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
    3. 마지막 도착 계단은 반드시 밟아야 한다.
- 따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.
- 각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.

- 입력: 입력의 첫째 줄에 계단의 개수가 주어진다. 둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다. 계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.
- 출력: 첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 출력한다.

예시
>> 6
10
20
15
25
10
20

출력: 75

"""


def solution(n, S):
    if n <= 2:
        return sum(S)
    dp = [0] * n
    dp[0] = S[0]
    dp[1] = S[0]+S[1]
    for i in range(2, n):
        dp[i] = max(S[i]+S[i-1]+dp[i-3], S[i]+dp[i-2])
    return dp[-1]

if __name__ == "__main__":
    n = int(input())
    S = [int(input()) for _ in range(n)]
    print(solution(n, S))

"""

Comment:

DP(n): n칸까지 올랐을 때 얻을 수 있는 최댓값
DP(n) = max(직전칸에서 올라온 경우의 최댓값, 전전칸에서 올라온 경우의 최댓값)
>> dp[i] = max(S[i]+S[i-1]+dp[i-3], S[i]+dp[i-2])

"""