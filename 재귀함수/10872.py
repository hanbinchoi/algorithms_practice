def factorial(n):
    if n > 1:
        return n*factorial(n-1)
    elif n == 0:
        return  1
    else:
        return n

n = int(input())

print(factorial(n))