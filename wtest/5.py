def solution(rows, columns):
    answer = [[0 for i in range(columns)]for i in range(rows)]

    answer[0][0] = 1
    now = 1
    r = 0
    c = 0
    visited = []
    while True:
        zCnt = 0
        for i in answer:
            zCnt += i.count(0)
        if zCnt == 0:
            break
        if now%2 == 1:
            prev_r = r
            prev_c = c
            c += 1
            if c == columns: c = 0
            if [prev_r,prev_c,r,c] in visited:
                answer[prev_r][prev_c] = now - len(visited)
                break
            visited.append([prev_r,prev_c,r,c])
        else:
            prev_r = r
            prev_c = c
            r += 1
            if r == rows: r = 0
            if [prev_r,prev_c,r,c] in visited:
                answer[prev_r][prev_c] = now - len(visited)
                break
            visited.append([prev_r,prev_c,r,c])
        now+=1
        answer[r][c] = now
    return answer

print(solution(10,7))