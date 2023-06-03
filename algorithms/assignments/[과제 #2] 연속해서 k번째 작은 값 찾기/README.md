# Stream of k-th smallest

* **입력**:
  * `n`개의 서로 다른 정수 값
  * `3 <= n <=100,000`
* **출력**:
  * `m[i]` 값을 `A[0]`, ..., `A[i]` 중 `i//3 + 1`번째로 작은 값으로 정의한다. 이 때 제일 작은 값은 `1`번째로 작다고 정의한다.
  * 모든 `i = 0`, ..., `n-1`에 대해, `m[i]` 값의 합을 출력한다.
* 여러 알고리즘이 존재한다. 수행 시간이 가능한 작도록 알고리즘을 설계하라.
  * 수행 시간이 빠를수록 높은 점수
  * 주석으로 다음 두 가지 내용을 반드시 기록하라 (주석 없으면 0점 처리)
    * 사용한 자료구조와 알고리즘을 간단히 설명하고
    * 수행 시간을 분석하고 Big-O로 표기
* **제한 시간**: 각 테스트 케이스의 제한 시간은 10초이다.
* **채점 기준**:
  * 테스트 케이스 통과 점수
  * 알고리즘의 정확성
  * 수행 시간의 효율성
  * 주석 - 알고리즘 설명과 수행 시간 분석 점수



## 코드

```python
# 이진 인덱스 트리를 활용했으며 O(nlogn)의 시간 복잡도를 갖습니다.
# Tree 클래스의 update와 query 함수는 각각 O(logn)의 복잡도를 가집니다.
# kth_smallest 함수에서 A를 반복하면서 각 요소에 대해 트리를 업데이트하고 k번째 작은 값을 찾습니다. 이때 A의 길이는 n이므로 n번 실행됩니다.
# 반복문 내에서 update와 find_kth_smallest 함수를 호춯하고 find_kth_smallest 함수는 이진 탐색을 수행하고 query 함수를 사용하므로 반복문 내부는 O(logn) 복잡도를 갖습니다.
# 따라서 전체 복잡도는 O(nlogn) 입니다.

class Tree:
	def __init__(self, size):
			self.size = size # 트리의 크기 저장
			self.tree = [0] * (size + 1) # 트리를 초기화

	def update(self, i, value):
			i += 1 # 인덱스의 값 조정 (본 트리의 인덱스 시작을 1로 할 것이기에..)
			while i <= self.size: # 트리 크기만큼 루프
					self.tree[i] += value # 값을 업데이트(갱신)
					i += i & -i # 다음 구간으로 이동

	# 인덱스 i까지의 배열 부분합을 계산하는 함수
	def query(self, i):
			i += 1 # 인덱스의 값 조정 (본 트리의 인덱스 시작을 1로 할 것이기에..)
			total_sum = 0 # 합 저장할 변수 초기화
			while i > 0: # 인덱스가 양수일 때
					total_sum += self.tree[i] # 합에 더함
					i -= i & -i # 이전 구간으로 이동
			return total_sum

	# k번째 작은 수를 구하는 함수
	def find_kth_smallest(self, k):
			lo, hi = 0, self.size # 이진 탐색 범범위 설정
			while lo < hi: # 범위 내를 루프
					mid = (lo + hi) // 2 # 중간값 설정
					if k <= self.query(mid): # 만약 중간값 기준으로 query한 것 (mid 인덱스까지의 배열 부분합)보다 작거나 같다면
							hi = mid # 상한 (hi)를 중간값으로 낮춤
					else: 
							lo = mid + 1 # 하한 (lo)를 중간값 다음 값으로 높임
			return lo


# k번째 작은 요소의 합을 구하는 함수
def kth_smallest(A):
	total_sum = 0 # 결과 저장할 변수 초기화
	bit = Tree(max(A) - min(A) + 1) # 트리 객체 생성 (A 내 모든 값을 담을 수 있도록 (A의 최대값 - A의 최솟값 + 1) 크기만큼 잡아줌)
	offset = min(A) # 오프셋 계산

	for i, num in enumerate(A): # A의 값마다 인덱스 (i)와 값(num)으로 루프
			bit.update(num - offset, 1) # 현재 값 추가. A의 가장 작은 값 (offset)을 빼줌으로써 가장 작은 값이 트리 내 인덱스 0에 올 수 있도록 함
			k = i // 3 + 1 
			kth_smallest_num = bit.find_kth_smallest(k) + offset # k번째 작은 요소 탐색
			total_sum += kth_smallest_num # 찾은 kth_smallest_num을 합계에 더함

	return total_sum

A = list(map(int, input().split()))
print(kth_smallest(A))
```

