a = {}

b = [19,4,2,5,3,9,7]

for index, number in enumerate(b):
    a[number] = index
print(a)
print(len(a))
try:
    print(a[1231])
except:
    print("not in list")

for element in a:
    print(element)