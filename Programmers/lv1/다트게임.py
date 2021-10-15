def calc_point(dartResult, cursor):
    p = ""
    for i in dartResult[cursor:]:
        if i.isdigit():
          p += i
        else:
            break

    if dartResult[cursor + len(p)] == "S":
        return [int(p) ** 1, len(p)]
    elif dartResult[cursor + len(p)] == "D":
        return [int(p) ** 2, len(p)]
    elif dartResult[cursor + len(p)] == "T":
        return [int(p) ** 3, len(p)]

def check_cursor(dartResult,cursor):
    if cursor >= len(dartResult):
        return True
    else:
        return False

def solution(dartResult):
    answer = 0
    cursor = 0
    point = []
    while True:
        if dartResult[cursor].isdigit():
            point.append(calc_point(dartResult,cursor)[0])
            cursor += calc_point(dartResult,cursor)[1]+1

        if check_cursor(dartResult, cursor): break
        if dartResult[cursor] == "*":
            if len(point) > 2:
                for i in range(len(point)-2,len(point)):
                    point[i] = point[i]*2
            else:
                point = [2*x for x in point]
            cursor += 1
        if check_cursor(dartResult, cursor): break

        if dartResult[cursor] == "#":
            point[-1] = -1 * point[-1]
            cursor += 1

        if check_cursor(dartResult, cursor): break


    return sum(point)

