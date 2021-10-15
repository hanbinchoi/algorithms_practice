def solution(sizes):
    answer = 0
    for i in sizes:
        if i[0] < i[1]:
            i[0],i[1] = i[1],i[0]
    width, height = 0,0
    for i in sizes:
        if width < i[0]:
            width = i[0]
        if height < i[1]:
            height = i[1]
    answer = width*height
    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))

