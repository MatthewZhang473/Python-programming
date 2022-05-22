depth = int(input())

array = [0]

for row in range(1,depth+1):
    for column in range(1,row+1):
        if column == 1 or column == row:
            temp = 1
        else:
            x = row-1
            y = column - 1
            pos1 = int(x*(x-1)/2) + y
            pos2 = pos1 + 1
            temp = array[pos1]+ array[pos2]
        array.append(temp)
for element in array[1:]:
    print(element,end = " ")