import sys

shape = input()
count = 0
result = 0

for i in range(len(shape)):
    if shape[i] == '(':
        count += 1
    elif shape[i] == ')':
        if shape[i-1] == '(':
            count -= 1
            result += count
        else:
            count -= 1
            result += 1

print(result)
