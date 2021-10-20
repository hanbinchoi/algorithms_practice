s, m = map(int,input().split())
time = 0
p = 0
sinho = [[]]
for i in range(s):
    d,r,g = map(int,input().split())
    time = time+d
    p = d

    while True:
        if r-time > 0:
            time += r-time
            break
