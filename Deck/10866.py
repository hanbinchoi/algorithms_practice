def solution(v):
    answer = []

    print('Hello Python')
    x,y= [],[]

    for i in v:
        x.append(i[0])
        y.append(i[1])
    while len(x) != 1:
        if x.count(x[0]) > 1:
            k = x[0]
            for i in range(x.count(x[0])):
                x.remove(k)
        else:
            x1 = x[0]
            break
        x1 = x[0]
    while len(y)!=1:
        if y.count(y[0]) >1:
            k = y[0]
            for i in range(y.count(y[0])):
                y.remove(k)
        else:
            y1=y[0]
            break
        y1 = y[0]

    return [x1,y1]

print(solution([[1, 4], [3, 4], [3, 10]]))