x = ['a','b','c','d','e','f','g','h']
y = [1,2,3,4,5,6,7,8]
x = list(map(ord, x))

data = input()
px,py = data[0], data[1]
px = ord(px)
py = int(py)

steps = [(2,1),(2,-1),(1,2),(1,-2),(-2,1),(-2,-1),(-1,-2),(-1,2)]

count = 0;
for i in steps:
    nx = px+i[0]
    ny = py+i[1]

    if (ny >= 1 and ny <= 8 and nx <= ord('h') and nx >= ord('a')):
        count += 1

print(count)