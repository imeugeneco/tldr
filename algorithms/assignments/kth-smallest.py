"""

- 입력: n 개의 서로 다른 정수 값이 들어있는 리스트 A (단 3<=n<=100,000)
- 출력: m[i]값을 A[0],...A[i] 중 (i//3+1)번째로 작은 값으로 정의할때 모든 i=0, ... n-1에 대해 m[i]값의 합
- 추가조건: heapq.nsmallest() 함수와 sort() 함수는 사용하면 안됨

Example 1
입력: 9 1 3 2 7 0 -2 4 5
출력: 19

Example 2
입력: 7 6 5 4 3 2 1
출력: 33

Example 3
입력: 11 12 -20 14 -10 -8 -7 -6 -4 -2 
출력: -38

"""


# Heap 사용 풀이
import heapq

def kth_smallest(A):
	heap = [] # heap 초기상태 선언
	total_sum = 0 # m[i] 값들의 합을 담을 변수 선언
	
	for i, num in enumerate(A): # 리스트 A의 각 요소에 대한 인덱스 (i), 값 (num)으로 루프
		heapq.heappush(heap,num) # heap에 현재 num 삽입
		k = i//3+1 # m[i]를 찾기 위한 인덱스 계산
		temp_heap = [] # pop된 요소를 보관하기위한 임시 heap 선언
		
		# heap에서 k번째로 작은 요소를 pop하기 위한 루프
		for _ in range(k): 
			kth_smallest_num = heapq.heappop(heap) 
			temp_heap.append(kth_smallest_num)
		
		# 마지막으로 저장된 kth_smallest_num 값이 곧 k번째 작은 요소.
		# 이것을 total_sum에 더함
		total_sum += kth_smallest_num  
		
		# 다음으로 돌 리스트 A의 범위를 위해 temp_heap에 있는 요소를 다시 heap에 삽입
		for element in temp_heap:
			heapq.heappush(heap, element)
		
	return total_sum

A = list(map(int,input().split()))
print(kth_smallest(A))



# 이진 인덱스 트리 풀이법: O(nlogn)
# Tree 클래스의 update와 query 함수는 각각 O(logn)의 복잡도를 가집니다.
# kth_smallest 함수에서 A를 반복하면서 각 요소에 대해 트리를 업데이트하고 k번째 작은 값을 찾습니다. 이때 A의 길이는 n이므로 n번 실행됩니다.
# 반복문 내에서 update와 find_kth_smallest 함수를 호출하고 find_kth_smallest 함수는 이진 탐색을 수행하고 query 함수를 사용하므로 반복문 내부는 O(logn) 복잡도를 갖습니다.
# 따라서 코드 전체 복잡도는 O(nlogn) 입니다.

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
