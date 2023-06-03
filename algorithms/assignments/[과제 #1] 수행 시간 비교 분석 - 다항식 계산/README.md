# 다항식 계산

* 전형적인 `n-1`차 다항식의 n개의 계수 (*coefficient*)가 리스트 `A`에 저장되어 있다고 하자.
  * `evaluate_n2(A,x)`: `f(x)`를 계산하고 그 값을 리턴하는 데, `O(n^2)`시간의 계산이 필요한 함수
  * `evaluate_n(A,x)`: `f(x)`를 계산하고 그 값을 리턴하는 데, `O(n)` 시간의 계산이 필요한 함수




## 코드

```python
import time, random

def evaluate_n2(A, x):
	# code for O(n^2)-time function
	n = len(A)
	res = 0
	for i in range(n):
		term = A[i]
		for j in range(i):
			term *= x
		res += term
	return res
			
	
def evaluate_n(A, x):
	# code for O(n)-time function
	n = len(A)
	res = 0
	x_powered = 1
	for i in range(n):
		res += (A[i] * x_powered)
		x_powered *= x
	return res
	
random.seed()	# random 함수 초기화

n = int(input())

# 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
A = [random.randint(-1000,1000) for _ in range(n)]
x = random.randint(-1000,1000)

# evaluate_n2 호출
sn2 = time.process_time()
evaluate_n2(A,x)
en2 = time.process_time()

# evaluate_n 호출
sn = time.process_time()
evaluate_n(A,x)
en = time.process_time()

# 두 함수의 수행시간 출력
print(f"evaluate_n2 수행시간: {en2-sn2}\nevaluate_n 수행시간: {en-sn}")


```



## 수행 시간 비교

| n      | evaluate_n2 (O(n2)) | evaluate_n (O(n))     |
| ------ | ------------------- | --------------------- |
| 1,000  | 0.076161223         | 0.000583409000000007  |
| 3,000  | 1.8192304289999999  | 0.0042284019999998534 |
| 5,000  | 8.327142208         | 0.017468863999999584  |
| 7,000  | 19.035101175999998  | 0.03422740299999916   |
| 9,000  | 38.274214754        | 0.05461145399999623   |
| 10,000 | 40.965572411        | 0.03242180099999814   |



1. **급격하게 증가하는 `evaluate_n2`의 실행 시간**

`evaluate_n2` 함수는 `O(n2)` 시간 복잡도를 가지기 때문에 `n`이 증가할수록 실행 시간이 급격하게 증가합니다. 이는 이중 반복문이 사용되어서 발생하는데, `n`이 `1 `증가할 때마다 반복문은 이전 `n`보다 `1`씩 더 반복하게 됩니다. 따라서 `n`이 커질수록 내부 반복문이 실행되는 횟수가 기하급수적으로 증가하여 실행 시간도 급격하게 증가하게 됩니다.

실행 결과를 보면 `n=1,000`일 때 `evaluate_n2` 함수의 실행 시간은 `0.076`초인 반면, `n=10,000`일 때는 `40.965`초로 대략 `500`배 이상 느려지는 것을 확인할 수 있습니다.



2. **비교적 변화 폭이 작은 `evaluate_n`의 실행 시간**

반대로 `evaluate_n` 함수는 `O(n)`의 시간 복잡도를 가지기 때문에 `n`이 증가하더라도 실행 시간의 변화 폭이 비교적 적습니다. 이 함수에서는 내부 반복문이 하나만 사용되기 때문에 `n`이 `1` 증가하면 내부 반복문이 `1`번씩 더 실행됩니다. 즉, `n`이 커져도 내부 반복문이 실행되는 횟수는 선형적으로 증가합니다.

예를 들어 `n=1,000`일 때 `evaluate_n`의 실행 시간은 `0.0005`초 수준인데, `n=10,000`일 때도 `0.032`초로 큰 차이가 없습니다. `evaluate_n2` 함수와 다르게 `n`이 커져도 실행 시간이 비교적 비슷하게 유지됩니다.



3. **`evaluate_n2`와 `evaluate_n` 결과 비교**

위 내용을 통해 시간 복잡도가 작은 `O(n)` 알고리즘이 입력 크기가 커질수록 효율적이라는 것을 알 수 있었습니다. 따라서 큰 데이터를 다룰 때는 `O(n)` 시간 복잡도를 가지는 `evaluate_n` 함수를 사용하는 것이 효율적일 것으로 판단됩니다.