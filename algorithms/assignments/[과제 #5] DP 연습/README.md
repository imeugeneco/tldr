# [#1] 최장 부문 부수열

* 영어 대문자로만 구성된 문자열이 입력으로 주어지면, 입력 문자열의 부수열 (*subsequence*) 중에서 가장 긴 회문 (*palindrome*)의 길이를 출력한다.
  * 입력 문자열의 길이는 `1`이상 `2,500` 이하이다.
  * 회문은 왼쪽에서 오른쪽으로 읽거나 반대로 오른쪽에서 왼쪽으로 읽어도 같은 단어를 의미한다 (예. radar, madam)
  * 회문의 길이는 회문 문자열의 길이이다 (예. radar는 길이가 `5`인 회문)
  * 한 문자는 길이가 `1`인 회문이다.
* **제한 시간**: 5초
* **주석**: 알고리즘을 간단히 설명하고 수행 시간을 분석하라.



## 코드

```python
def longest_palindrome(s):
	n = len(s)
	# dp[i][j]는 s[i:j+1]의 부분 문자열에서 가장 긴 회문의 길이를 저장
	dp = [[0] * n for _ in range(n)]

	# 모든 문자는 길이가 1인 회문이므로, dp[i][i]를 1로 초기화
	for i in range(n):
			dp[i][i] = 1

	# 길이가 2 이상인 회문을 찾음
	for length in range(2, n + 1):
			for i in range(n - length + 1):
					j = i + length - 1
					if s[i] == s[j]:
							# 첫 번째와 마지막 문자가 같다면, dp[i][j]는 안쪽 문자열의 회문에 2를 더한 값
							dp[i][j] = dp[i + 1][j - 1] + 2
					else:
							# 첫 번째와 마지막 문자가 다르다면, dp[i][j]는 두 부분 문자열의 최대 회문 길이 중 큰 값
							dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

	# 전체 문자열에서 가장 긴 회문의 길이를 반환
	return dp[0][n - 1]

str = input()
print(longest_palindrome(str))
```

<br></br>

# [#2] 왼쪽 맞춤

* 아래한글이나 MS Word에서는 문단을 왼쪽 맞춤, 오른쪽 맞춤, 양쪽 맞춤 중 하나로 편집가능하다. 그 중에서 왼쪽맞춤을 생각해보자.

  * 각 줄의 처음은 단어로 시작하고, 두 단어 사이에는 정확히 하나의 공백(*space*)를 넣는다고 가정한다.
  * 단어 하나는 반드시 한 줄에 포함되어야 한다. 즉, 두 줄에 걸쳐 나뉘어 나타나지 않아야 한다.

* 문장을 페이지 폭이 `W`인 쪽(*page*)에서 왼쪽 맞춤을 예쁘게 하기 위해, 각 줄마다 penalty 점수를 `(W - 해당 줄의 글자 수 - 단어 사이의 공백 수)**3` 으로 정의한다.

  * 예. `[Ape ate apple.  ]`에서 `W` = `16`이고, 글자수 = `12` (마침표 포함), 세 단어 사이의 공백 수 = `2` 이므로 `(16-14)**3 = 8`점이 penalty 값이다.

* 최종 왼쪽 맞춤의 penalty 값은 각 줄의 penalty 값의 합으로 정의된다.

* **입력**: `W`값을 첫 번째 줄에서 먼저 입력받고 두 번째 줄에서 여러 문장을 한 줄로 입력받는다.

  * 입력 받은 문장을 공백 기준으로 `split` 분할하여, 폭이 `W`인 페이지에 왼쪽 맞춤을 하는데, penalty값이 최소가 되도록 한다.
  * 단, `W`값은 가장 긴 단어 (구둣점 포함)의 길이보다 같거나 크다고 가정해도 된다.

* **출력**: 최소 penalty 값

* **분석**: 코드 마지막에 주석으로 점화식을 쓰고 알고리즘의 수행 시간을 간단하게 분석한 후 Big-O 기호로 표기할 것

* 입력 예: `W=8`인 경우

  > 8
  >
  > ape eats apple cider a lot.

  * 이 때 최소 penalty `62`가 되고 그 때의 왼쪽 맞춤한 결과는 아래와 같다 (마지막 문자 `|`은 줄의 마지막임을 나타내기 위해 일부러 삽입한 것)

  > ape eats|
  >
  > apple   |
  >
  > cider   |
  >
  > a lot.  |

  * 첫 줄의 `penalty = 0`, 둘째 줄의 `penalty = 3^3 = 27`, 세째 줄의 `penalty = 3^3 = 27`, 네째 줄의 `penalty = 2^3 = 8`이 되어 `62`가 되고, 이 값이 입력에 대한 최소 penalty의 왼쪽 맞춤이 된다.
  * 만약 아래처럼 왼쪽 맞춤을 하면, 총 `penalty = 0 + 3^3 + 1^3 + 4^3 = 92`가 되어 최소 penalty를 갖는 왼쪽 맞춤이 아니다.

  > ape eats|
  >
  > apple   |
  >
  > cider a |
  >
  > lot.    |

* 최소 penalty가 되는 왼쪽 맞춤은 여러 개가 존재할 수도 있다. 즉, 최소 penalty값은 유일하지만, 그 penalty값을 주는 왼쪽 맞춤은 여러 개일 수 있다.



## 코드

```python
W = int(input())
words = input().split()
# code below
def min_penalty(W, words):
	n = len(words) 
	penalty = [0]*(n+1)  # 각 단어에 대한 페널티 값을 저장할 리스트 초기화
	line_cost = [0]*(n+1)  # 각 줄에 대한 비용 값을 저장할 리스트 초기화

	penalty[n] = 0  # 마지막 줄의 페널티는 0
	line_cost[n] = 0  # 마지막 줄의 비용은 0

	# 단어 리스트를 거꾸로 탐색
	for i in range(n-1, -1, -1):
		line_cost[i] = float('inf')  # 현재 줄의 비용을 무한대로 설정
		length = -1  # 각 단어 사이에는 공백이 있으므로 공백을 고려한 길이를 -1로 시작
		for j in range(i, n):
				length += len(words[j]) + 1  # 단어와 공백의 길이를 더함
				if length > W:  # 만약 길이가 줄의 너비를 초과하면 break
						break
				# 현재 페널티는 (W-length)^3 + 다음 줄의 페널티
				cur_penalty = (W-length)**3 + penalty[j+1]  
				if cur_penalty < line_cost[i]:  # 만약 현재 페널티가 현재 줄의 비용보다 작으면 업데이트
						line_cost[i] = cur_penalty
		penalty[i] = line_cost[i]  # 최소 페널티로 업데이트
	return penalty[0]  # 첫 단어를 시작으로 하는 최소 페널티를 반환

print(min_penalty(W, words))


# DP 점화식:
# penalty[i] = min((W - length)^3 + penalty[j+1]) for all i <= j < n
# 여기서 length는 i번째 단어부터 j번째 단어까지의 총 길이입니다.

# 각 단어에 대해 모든 가능한 다음 단어를 확인하기 때문에 이 알고리즘의 시간 복잡도는 O(n^2)입니다. 이 때 n은 입력된 단어의 수입니다. 이는 최악의 경우 각 단어에 대해 모든 가능한 다음 단어를 확인해야 하므로 이러한 시간 복잡도가 발생합니다.
```

