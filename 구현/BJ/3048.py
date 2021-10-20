# 3048, 개미
import sys

N1, N2 = map(int, sys.stdin.readline().split())
ants1 = list(sys.stdin.readline().rstrip())
ants2 = list(sys.stdin.readline().rstrip())
T = int(sys.stdin.readline())

dir = {}	# 방향 저장
for ant in ants1:
    dir[ant] = 0    # 뒤로 이동
for ant in ants2:
    dir[ant] = 1    # 앞으로 이동

ants1.reverse()
ants1.extend(ants2)
print(dir)
for _ in range(T):
    i = 0
    while i < len(ants1)-1:
        print(ants1[i])
        if dir[ants1[i]] == 0 and dir[ants1[i+1]] == 1:
            ants1[i], ants1[i+1] = ants1[i+1], ants1[i]
            i += 1
        i += 1
    print("--")
for ant in ants1:
    print(ant, end='')