def solution(input):
    first = -1
    second = -1

    for i in range(len(input)):
        if input[i].isdigit():
            val = int(input[i])
            if val> first:
                second = first
                first = val
    return second

