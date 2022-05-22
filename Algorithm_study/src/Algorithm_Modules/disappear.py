# print("this is a debug message")

def solution(N, A, B):
    edges = [[] for i in range(N)]
    unused = [True for i in range(N)]

    for i in range(len(A)):
        edges[A[i]].append(B[i])
        edges[B[i]].append(A[i])
    

    dis = True

    counter = -1

    while dis == True:
        counter += 1
        dis = False
        for i in range(N):
            if unused[i] == False:
                continue
            elif len(edges[i]) == 0:
                dis = True
                unused[i] = False
            elif len(edges[i]) == 1:

                dis = True
                unused[i] = False
                the_other_point = edges[i][0]
                edges[the_other_point].remove(i)
        

    return counter

print(solution(7, [0, 1, 2, 4, 5], [1, 2, 3, 5, 6]))
