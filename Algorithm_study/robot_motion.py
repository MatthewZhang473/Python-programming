


def solution(directions):
    commands = ["L", "R","F"]
    rot = ["L", "R"]
    rot_angle = 0
    position = [0,0]
    counter = 0

    for i in range(len(directions)):
        if directions[i] not in commands:
            continue
        else:
            if directions[i] in rot:
                rot_angle = angle_calc(directions[i],rot_angle)
            else:
                delta = motion(rot_angle)
                position[0] += delta[0]
                position[1] += delta[1]
    
    counter = abs(position[0])+abs(position[1])
    
    
    rightward = rot_angle
    upward = rot_angle

    if position[0] > 0:
        rightward = 2
    elif position[0] < 0:
        rightward = 0

    if position[1] >0:
        upward = 3
    elif position[1] <0:
        upward = 1

    
    temp = max(diff(rightward,rot_angle),diff(upward,rot_angle))
    counter += min(2,temp)

    return counter

def diff(r1,r2):
    tempo = abs(r1-r2)
    return min(tempo,4-tempo)


def motion(angle):
    if angle == 0:
        return [1,0]
    if angle == 1:
        return [0,1]
    if angle == 2:
        return [-1,0]
    if angle == 3:
        return [0,-1]

def angle_calc(dir,angle):
    if dir == "L":
        return (angle + 1)%4
    else:
        return (angle - 1)%4

print(solution("FF"))