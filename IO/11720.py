import sys

t = int(input())
number = input()
sum = 0;
try:
    if t==len(number):
        for i in range(len(number)):
            sum += int(number[i]);
    print(sum)
except Exception as e:
    print(e)