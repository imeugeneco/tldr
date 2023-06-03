# Quick, Merge, Heap 정렬 비교하기

* Quick, Merge, Heap 정렬을 모두 구현해보고, 시간과 비교 및 교환/이동 횟수를 다양한 `n`에 대해 실행하여 비교한다.
* 세 가지 정렬 알고리즘을 작성하라:
  * `quick_sort(A, first, last): A[first] ... A[last]`까지 quick sort하는 함수
  * `merge_sort(A, first, last): A[first] ... A[last]`까지 merge sort하는 함수
  * `heap_sort(A)`: `A`의 값들을 heap sort하는 함수 (`heap` 클래스 정의할 필요는 없으며 `heapq` 모듈 사용 금지)
* 추가로 고려할 사항:
  * **[추가 점수 1: quick sort]** 굳이 하나가 남을 때까지 분할할 필요는 없음. 경우에 따라서 `10`과 `40` 사이의 상수 `K`에 대해 `K`개 이하가 되면 분할을 멈추고 insertion sort로 정렬을 하면 더 빠를 수 있음. 이 방법을 구현하여 비교해 보아라.
  * **[추가 점수 2: quick sort]** 적당한 `K`개가 남을 때까지만 분할한 후, 따로 insertion sort 등으로 정렬을 하지 않는다면, 전체 값이 완전히 정렬이 되지는 않지만 대부분 정렬이 된 상태가 된다. 완전히 정렬하기 위해, 전체 값들을 대상으로 insertion sort를 적용할 수도 있음. 이 방법을 구현하여 비교해 보아라.
  * **[추가 점수 3: merge sort]** 왼쪽 반과 오른쪽 반으로 나누지 않고, 3등분하여 재귀적으로 정렬한 후 merge하는 `3-way merge sort` 알고리즘도 구현하여 함께 비교해 보아라.
  * **[추가 점수 4: Tim sort]** python의 sort 함수는 Tim sort 알고리즘을 구현한 것이다. 이 함수의 수행 시간을 다른 세 가지 알고리즘의 수행 시간과 비교해 보아라.
* 랜덤한 수를 `n`개 생성하여, 리스트에 저장, 세 개의 정렬 함수를 호출해 정렬하고 다음 세 값을 각각 기록하라:
  * **수행 시간**: `timeit` 모듈 이용
  * 비교 횟수: 두 수를 비교하는 횟수
  * **교환과 이동횟수**: 두 수를 교환(*swap*)하거나 하나의 수를 이동(*move*)한 횟수 (merge정렬에서의 이동 횟수 포함)
  * 단, Tim sort의 경우에는 수행 시간만 측정할 수 있기 때문에, 비교 횟수와 교환/이동 횟수 비교는 제외
  * `n`의 값을 `100, 500, 1000, 5000, 10000, 50000, 100000, 500000` 정도까지 다양하게 변화하면서 위의 세 가지 값이 어떻게 변하는지 기록하고 그 결과를 분석한 후 개인적인 느낌을 자유롭게 작성하라.

## 코드

```python
import random, timeit

def quick_sort(A, first, last):
	global Qc, Qs
	if first >= last:
			return A
	left, right = first + 1, last
	pivot = A[first]
	while left <= right:
			while left <= right and A[left] < pivot:
					left += 1
					Qc += 1
			while right > first and A[right] > pivot:
					right -= 1
					Qc += 1
			if left <= right:
					A[left], A[right] = A[right], A[left]
					Qs += 1
					left += 1
					right -= 1
	A[first], A[right] = A[right], A[first]
	Qs += 1
	quick_sort(A, first, right - 1)
	quick_sort(A, right + 1, last)
	
def insertion_sort(A, first, last):
	for i in range(first + 1, last + 1):
			key = A[i]
			j = i - 1
			while j >= first and A[j] > key:
					A[j + 1] = A[j]
					j -= 1
			A[j + 1] = key

def quick_sort2(A, first, last, K):
	if first >= last:
			return A
	if last - first <= K:
			insertion_sort(A, first, last)
	else:
			left, right = first + 1, last
			pivot = A[first]
			while left <= right:
					while left <= right and A[left] < pivot:
							left += 1
					while right > first and A[right] > pivot:
							right -= 1
					if left <= right:
							A[left], A[right] = A[right], A[left]
							left += 1
							right -= 1
			A[first], A[right] = A[right], A[first]
			quick_sort2(A, first, right - 1, K)
			quick_sort2(A, right + 1, last, K)

def merge_sort(A, first, last):
	if first >= last:
			return A
	merge_sort(A, first, (first+last)//2)
	merge_sort(A, (first+last)//2 + 1, last)
	merge_two_sorted_lists(A, first, last)

def merge_two_sorted_lists(A, first, last):
	global Mc, Ms
	m = (first + last) // 2
	i, j = first, m + 1
	B = []
	while i <= m and j <= last:
			Mc += 1
			if A[i] <= A[j]:
					B.append(A[i])
					i += 1
			else:
					B.append(A[j])
					j += 1
			Ms += 1
	for k in range(i, m + 1):
			B.append(A[k])
			Ms += 1
	for k in range(j, last + 1):
			B.append(A[k])
			Ms += 1
	for i in range(first, last + 1):
			A[i] = B[i - first]

def merge_three_sorted_lists(A, first, mid1, mid2, last):
	i, j, k = first, mid1 + 1, mid2 + 1
	B = []
	while i <= mid1 and j <= mid2 and k <= last:
			if A[i] <= A[j] and A[i] <= A[k]:
					B.append(A[i])
					i += 1
			elif A[j] <= A[i] and A[j] <= A[k]:
					B.append(A[j])
					j += 1
			else:
					B.append(A[k])
					k += 1

	while i <= mid1 and j <= mid2:
			if A[i] <= A[j]:
					B.append(A[i])
					i += 1
			else:
					B.append(A[j])
					j += 1

	while j <= mid2 and k <= last:
			if A[j] <= A[k]:
					B.append(A[j])
					j += 1
			else:
					B.append(A[k])
					k += 1

	while i <= mid1 and k <= last:
			if A[i] <= A[k]:
					B.append(A[i])
					i += 1
			else:
					B.append(A[k])
					k += 1

	while i <= mid1:
			B.append(A[i])
			i += 1

	while j <= mid2:
			B.append(A[j])
			j += 1

	while k <= last:
			B.append(A[k])
			k += 1

	for i in range(first, last + 1):
			A[i] = B[i - first]

def three_way_merge_sort(A, first, last):
	if first >= last:
			return A
	mid1 = first + (last - first) // 3
	mid2 = first + 2 * (last - first) // 3
	three_way_merge_sort(A, first, mid1)
	three_way_merge_sort(A, mid1 + 1, mid2)
	three_way_merge_sort(A, mid2 + 1, last)
	merge_three_sorted_lists(A, first, mid1, mid2, last)

def heap_sort(A):
	n = len(A)

	for i in range(n-1, -1, -1):
			heapify_down(A, i, n)

	for i in range(n - 1, 0, -1):
			A[0], A[i] = A[i], A[0]
			heapify_down(A, 0, i)

	return A


def heapify_down(A, k, n):
	global Hc, Hs
	while 2 * k + 1 < n:
			L, R = 2 * k + 1, 2 * k + 2
			Hc += 1
			if L < n and A[L] > A[k]:
					m = L
			else:
					m = k
			Hc += 1
			if R < n and A[R] > A[m]:
					m = R
			if m != k:
					A[k], A[m] = A[m], A[k]
					Hs += 1
					k = m
			else:
					break

# 아래 코드는 바꾸지 말 것!

def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
#
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000,1000))
B = A[:]
C = A[:]
D = A[:]
E = A[:]
F = A[:]

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))

print("")
print("Quick sort (insertion sort):") # 추가 과제: Quick sort
print("time =", timeit.timeit("quick_sort2(B, 0, n-1, 20)\n", globals=globals(), number=1))

print("")
print("Merge sort:")
print("time =", timeit.timeit("merge_sort(C, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("")
print("3-Way Merge sort:")
print("time =", timeit.timeit("three_way_merge_sort(D, 0, n-1)\n", globals=globals(), number=1))

print("")
print("Heap sort:")
print("time =", timeit.timeit("heap_sort(E)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

print("")
print("Tim sort:") # 추가 과제: Tim sort
print("time =", timeit.timeit("F.sort()", globals=globals(), number=1))

# 정렬되었는지 check한다
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))
assert(check_sorted(D))
assert(check_sorted(E))
assert(check_sorted(F))
```

<br></br>

## 정렬 알고리즘 성능 비교 분석

**6가지 알고리즘의 수행시간, 비교 횟수, 교환과 이동 횟수, 수행시간 비교**

| **n**       | **Quick Sort** |           | **Insertion Sort** |               |          |
| ----------- | -------------- | --------- | ------------------ | ------------- | -------- |
|             | **Time**       | **Comp**  | **Swap**           | **Comp+Swap** | **Time** |
| **100**     | 0.000117       | 421       | 166                | 587           | 0.000111 |
| **500**     | 0.001573       | 2,777     | 1,126              | 3,903         | 0.000635 |
| **1,000**   | 0.003401       | 7,174     | 2,449              | 9,623         | 0.001444 |
| **5,000**   | 0.019094       | 43,277    | 16,191             | 59,468        | 0.008588 |
| **10,000**  | 0.027138       | 91,153    | 36,540             | 127,693       | 0.018643 |
| **50,000**  | 0.301037       | 476,186   | 233,137            | 709,323       | 0.125494 |
| **100,000** | 0.820366       | 1,007,962 | 513,854            | 1,521,816     | 0.284178 |
| **500,000** | 2.903894       | 4,442,263 | 3,163,065          | 7,605,328     | 1.678613 |

| **n**       | **Merge Sort** |           | **3-Way Merge Sort** |               |          |
| ----------- | -------------- | --------- | -------------------- | ------------- | -------- |
|             | **Time**       | **Comp**  | **Swap**             | **Comp+Swap** | **Time** |
| **100**     | 0.000294       | 550       | 672                  | 1,222         | 0.000254 |
| **500**     | 0.004155       | 3,856     | 4,488                | 8,344         | 0.001263 |
| **1,000**   | 0.011078       | 8,703     | 9,976                | 18,679        | 0.002659 |
| **5,000**   | 0.0276         | 55,199    | 61,808               | 117,007       | 0.016235 |
| **10,000**  | 0.094027       | 120,450   | 133,616              | 254,066       | 0.036894 |
| **50,000**  | 0.59013        | 718,191   | 784,464              | 1,502,655     | 0.262322 |
| **100,000** | 1.493559       | 1,536,441 | 1,668,928            | 3,205,369     | 0.610641 |
| **500,000** | 6.490155       | 8,836,731 | 9,475,712            | 18,312,443    | 3.288675 |

| **n**       | **Heap Sort** |            | **Tim Sort** |               |          |
| ----------- | ------------- | ---------- | ------------ | ------------- | -------- |
|             | **Time**      | **Comp**   | **Swap**     | **Comp+Swap** | **Time** |
| **100**     | 0.000286      | 1,036      | 490          | 1,526         | 0.000009 |
| **500**     | 0.003793      | 7,448      | 3,546        | 10,994        | 0.000045 |
| **1,000**   | 0.015665      | 16,868     | 8,072        | 24,940        | 0.000096 |
| **5,000**   | 0.030393      | 107,702    | 52,091       | 159,793       | 0.001314 |
| **10,000**  | 0.119167      | 235,308    | 114,119      | 349,427       | 0.001240 |
| **50,000**  | 0.997942      | 1,409,634  | 687,330      | 2,096,964     | 0.035862 |
| **100,000** | 1.336823      | 3,019,014  | 1,474,605    | 4,493,619     | 0.015919 |
| **500,000** | 14.064946     | 17,394,816 | 8,522,115    | 25,916,931    | 0.103175 |



**수행시간**

* Worst case의 경우 `O(n^2)`의 시간 복잡도를 갖는 Quick sort가 실행 결과 실질적으로 Merge sort와 Heap sort에 비해 빠릅니다.
* 특히 `n`이 `100,000` 이상인 경우, Quick sort는 다른 두 알고리즘에 비해 훨씬 빠르게 수행됩니다.

**비교횟수**

* `n`이 커질수록 비교 횟수는 Heap sort에서 가장 높게 나타나고, 그 다음으로 Merge sort, 마지막으로 Quick sort 순으로 나타납니다.
* 모든 알고리즘에서 비교 횟수는 `n`에 대해 선형 증가하고, `n`이 증가할수록 비교 횟수가 증가합니다.

**스왑/이동횟수**

* `n`이 커질수록 스왑/이동 횟수는 Merge sort에서 가장 높게 나타나고, 그 다음으로 Heap sort, 마지막으로 Quick sort 순으로 나타납니다.
* 모든 알고리즘에서 스왑/이동 횟수는 `n`에 대해 선형 증가하고, `n`이 증가할수록 스왑/이동 횟수가 증가합니다.

이러한 차이들은 각 알고리즘의 작동 원리와 복잡도에 기인합니다. Quick sort는 일반적으로 평균적인 경우에 가장 빠른 정렬 알고리즘으로 알려져 있지만, 최악의 경우에는 성능이 떨어질 수 있습니다 (평균 `O(nlogn)`, 최악의 경우 `O(n^2)` 시간 복잡도를 갖음). 반면 Merge sort와 Heap sort는 보다 안정적인 성능을 제공하지만, 이로 인해 추가적인 리소스를 사용할 수 있습니다.

 

**[추가 과제 1]** Quick sort와 Insertion sort를 결합한 `quick_sort2()` 알고리즘의 경우 일반적으로 `K` 값이 적절하게 설정되면 quick sort의 성능을 개선할 수 있습니다. `K` 값에 따라 성능이 다소 변동할 수 있지만 위 표는 `K=20` 에 기인하여 도출된 결과값입니다.

**[추가 과제 2]** 왼쪽 반과 오른쪽 반으로 나누지 않고 3등분해서 재귀적으로 정렬한 후 Merge 하는 `three_way_merge_sort()` 알고리즘에선 Merge Sort의 수행시간이 약 반절 정도로 감소합니다.

**[추가 과제 3]** 입력 데이터의 특성에 따라 달라질 수 있지만, Python의 기본 정렬 알고리즘인 Tim Sort는 다른 정렬 알고리즘에 비해 월등한 성능을 보입니다.