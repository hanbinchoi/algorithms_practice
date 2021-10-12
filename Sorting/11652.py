import sys

num = int(sys.stdin.readline())
dict = {}
for i in range(num):
    n = int(sys.stdin.readline())
    if n in dict:
        dict[n] += 1
    else:
        dict[n] = 1

result = sorted(dict.items(), key=lambda x:(-x[1]))

print(result[0][0])
