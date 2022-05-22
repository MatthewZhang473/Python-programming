import random

A = [random.randint(0,1000) for i in range(100000000)]

ans = 0
A_set = set(A)

dic = {}
for element in A_set:
    dic[element] = 0

for element in A:
    dic[element] += 1

for key in dic.keys():
    ans += min(dic[key],abs(key-dic[key]))

print(ans)