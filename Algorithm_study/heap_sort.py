from heapq import heapify


def Heapify(A,heap_size,i):
    l = 2*i
    r = 2*i +1
    largest = i
    if l<= heap_size and A[l]>A[i]:
        largest = l
    if r<=heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        Heapify(A,heap_size,largest)

def Build_heap(A):
    heap_size = len(A)-1
    for i in range(int(heap_size/2),0,-1):
        Heapify(A,heap_size,i)

def Heap_sort(A):
    Build_heap(A)
    for i in range(len(A)-1,0,-1):
        temp = A[i]
        A[i] = A[1]
        A[1] = temp
        Heapify(A,i-1,1)



a = [0,16,4,10,14,7,9,3,2,8,1]

Heap_sort(a)

print(a)