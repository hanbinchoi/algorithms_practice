import sys

num = int(sys.stdin.readline())
check_num = [0] * 10001;

for i in range(num):
    number = (int(sys.stdin.readline()))
    check_num[number] += 1

for i in range(10001):
    if check_num[i] != 0:
        for j in range(check_num[i]):
            print(i)