"""

- 리스트 A의 값을 오름차순으로 정렬한 후, 실수로 왼쪽 방향으로 몇 번 rotation 이동을 했다. 예를 들어, 원래 A=[5,8,9,15,18,20,31]이었는데, 왼쪽으로 3번의 rotation을 하면 A=[15,18,20,31,5,8,9]가 된다.
- 입력: 서로 다른 n개의 값을 오름차순으로 정렬 후 k번 왼쪽 회전을 한 리스트 A (1 <= n <= 100,000, A의 값은 -20만과 +20만 사이)
- 출력: A에 대한 회전 횟수 k값 (단, k는 0이상 n-1이하이다. k=0인 경우는 회전이 없는 경우이고, k=n-1이면 회전을 가장 많이 한 경우이다)
- 목표: k값을 찾기 위한 비교 연산의 횟수를 최대한 줄이는 것
- 주석에 자신의 알고리즘의 비교 횟수를 분석한 후, Big-O 시간으로 표기한다.
- 제한시간: 1초

Example 1
Input: 5 6 1 2 3 4
Output: 4

Example 2
Input: 1 3 5 6 7 9
Output: 8

"""

# 이 문제는 오름차순이 끊기는 지점을 찾고 그 지점으로부터 리스트의 끝까지 숫자의 개수를 계산하여 해결할 수 있습니다. 
# T(n) = T(n/2) + c
# 이 알고리즘의 시간 복잡도는 분할 정복 전략을 사용하므로 O(logn)입니다. 배열을 절반씩 줄여나가면서 끊어지는 지점을 찾기 때문에 전체 원소 개수가 두 배로 늘어날 때마다 한 단계의 추가 작업만이 필요합니다. 따라서 배열의 크기에 대한 로그 스케일 복잡도를 가집니다.

def find_breaking_point(arr, left, right):
	# 범위 내에 원소가 하나만 있는 경우 (즉, left == right일 때)
	if left == right:
		return None
	
	# 범위 내 중간지점 계산
	mid = (left + right) // 2

	# 오름차순 끊기는 지점이 mid라면 mid 반환
	if arr[mid] > arr[mid-1] and arr[mid] > arr[mid + 1]:
			return mid
	# 혹은 mid 값이 맨 왼쪽 값보다 작다면
	elif arr[mid] < arr[left]:
		# 맨 왼쪽부터 mid 지점까지 새 범위 정의해서 재귀
		return find_breaking_point(arr, left, mid)
	else:
		# mid+1 부터 맨 오른쪽까지 새 범위 정의해서 재귀
		return find_breaking_point(arr, mid + 1, right)

def count_numbers_from_breaking_point(arr):
	breaking_point = find_breaking_point(arr, 0, len(arr) - 1)
	if breaking_point == None: return 0
	return len(arr) - breaking_point - 1

A = [int(x) for x in input().split()]
print(count_numbers_from_breaking_point(A))
