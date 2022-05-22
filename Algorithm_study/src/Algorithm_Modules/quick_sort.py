
def Quick_sort(A,l,r):
    if l<r:
        pos = partition(A,l,r)
        print(pos)
        Quick_sort(A,l,pos-1)
        Quick_sort(A,pos+1,r)

def partition(A,l,r):
    i = l-1
    piv = A[r]
    for j in range(l,r-1+1):
        if A[j]<=piv:
            i+=1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
        temp = A[i+1]
        A[i+1] = A[r]
        A[r] = temp
    return i+1
A = [1,4,2,4,7,2,8,4,6,7,13,4]

Quick_sort(A,0,len(A)-1)
print(A)