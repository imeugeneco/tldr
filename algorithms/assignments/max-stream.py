"""

- n개의 정수를 입력 받아 리스트 A에 저장 (정수 값의 범위는 -1,000 이상, +1,000 이하)
- A에 저장된 정수들에 대해, A[i] + A[i+1] + ... + A[j-1] + A[j] 값이 최대가 되는 i <= j 를 계산한 후, 그 최대값을 출력한다
- 반드시 분할정복 방법으로 구현해야 함
- 간략히 알고리즘을 설명하고, T(n)의 점화식과 최종 수행시간을 Big-O로 표기할 것

Example 1
Input: 0 -2 -2 -1 -4 4 1 0 -5 
Output: 5

Example 2
Input: -1 3 2 -1 4 3 5 3 4 5 -2 
Output: 28

"""

# 점화식: T(n) = 2 * T(n/2) + O(n)
# 최종 수행시간: O(nlogn)

def max_sum(A, left, right):
	# 만약 left와 right가 같다면 (배열의 크기가 1), 현재 인덱스 값 반환
	if left >= right:
		return A[left]
	
	# 왼, 오른쪽으로 분활하기 위한 중간 인덱스 계산
	mid = (left+right)//2
	
	# 왼쪽의 최대합 구하기 (재귀)
	leftArraySum = max_sum(A,left,mid)
	
	# 오른쪽의 최대합 구하기 (재귀)
	rightArraySum = max_sum(A,mid+1,right)
	
	# 중간부분을 포함하는 최대합 구하기
	leftSum = 0
	leftMax = float("-inf") # 음의 무한대
	for i in range(mid,left-1,-1):
		leftSum += A[i]
		if leftMax < leftSum:
			leftMax = leftSum
	
	rightSum = 0
	rightMax = float("-inf") # 음의 무한대
	for i in range(mid+1,right+1):
		rightSum += A[i]
		if rightMax < rightSum:
			rightMax = rightSum

	midMax = leftMax + rightMax # 중간 인덱스를 포함하는 최대합
	
	# 왼쪽, 오른쪽, 중간 값을 비교해서 가장 큰 값 반환
	if leftArraySum >= rightArraySum and leftArraySum >= midMax: 
		return leftArraySum
	elif rightArraySum >= leftArraySum and rightArraySum >= midMax: 
		return rightArraySum
	return midMax
	

A = [int(x) for x in input().split()]
sol = max_sum(A, 0, len(A)-1)
print(sol)

