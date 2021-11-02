import sys

value = 0
index = 0
for i in range(9):
    num = int(sys.stdin.readline())
    if value<num:
        value = num
        index = i

print(value)
print(index+1)