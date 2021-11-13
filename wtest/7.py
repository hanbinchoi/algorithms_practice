def rotate_right(n,m,result,template):
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = template[i][j]

def rotate_left(n,m,result,template):

    for i in range(n):
        for j in range(m):
            result[-j-1][i] = template[i][j]

def getRightResult(result):
    answer = []
    k = 1

    for i in range(0, len(result), 2):
        cnt = 2 * (k) - 1
        r = i
        c = 0
        line = ""
        check = True
        while cnt != 0:
            line += result[r][c]
            cnt -= 1
            if check:
                r -= 1
                check = False
            else:
                c += 1
                check = True

        answer.append(line)
        k += 1
    return answer

def getLeftResult(result):
    answer = []
    k = 1

    for i in range(0, len(result), 2):
        cnt = 2 * (k) - 1
        r = k-1
        c = len(result[0])-k

        line = ""
        check = True
        while cnt != 0:
            line += result[r][c]
            cnt -= 1
            if check:
                c += 1
                check = False
            else:
                r += 1
                check = True

        answer.append(line)
        k += 1
    return answer

def solution(grid, clockwise):

    maxLen = 0

    for i in grid:
        if maxLen<len(i):
            maxLen = len(i)

    template = []
    for i in grid:
        if len(i)<maxLen:
            k = (maxLen-len(i)) // 2
            temp = (k*"*")+i+(k*"*")
            template.append(list(temp))
        else:
            template.append(list(i))


    n = len(template)
    m = len(template[0])

    result = [[0] * n for _ in range(m)]

    if clockwise:
        rotate_right(n,m,result,template)
        answer = getRightResult(result)
    else:
        rotate_left(n, m, result, template)
        answer = getLeftResult(result)

    return answer

print(solution(["A"],	False))