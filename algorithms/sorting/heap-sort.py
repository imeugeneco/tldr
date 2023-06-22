"""

Heap & Heap Sort

- 힙 클래스를 선언한 후, 함수 heapify_down, make_heap, heap_sort를 구현한다.
- 한 줄에 정수 여러 개를 받아 리스트에 저장한 후, heap_sort를 호출한 후 정렬된 값을 출력한다.


"""

class Heap:
    def __init__(self, L=[]):
            self.A = L
            self.make_heap()

    def __str__(self):
            return str(self.A)

    def heapify_down(self, k, n):
            A = self.A
            while k < n // 2:
                    L, R = 2*k+1, 2*k+2
                    m = k 

                    if L < n and A[L] > A[m]:
                            m = L

                    if R < n and A[R] > A[m]: 
                            m = R

                    if k != m:
                            A[k], A[m] = A[m], A[k]
                            k = m
                    else:
                            break

    def make_heap(self):
            A = self.A
            n = len(A)
            for k in range(n-1, -1, -1):
                    self.heapify_down(k, n)

    def heap_sort(self):
            A = self.A
            n = len(A)
            for i in range(n-1, -1, -1):
                    self.heapify_down(0, i+1)
                    A[0], A[i] = A[i], A[0]
            return A

L = [int(x) for x in input().split()]
H = Heap(L)
H.heap_sort()
print(H)
