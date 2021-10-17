import sys
sys.setrecursionlimit(10**7)

dp = [0] * 100002

def fibo(n):
    if n == 2:
        return 1

    if n ==  1:
        return 1

    if dp[n] != 0 :
        return dp[n]
    dp[n] = fibo(n-2)+fibo(n-1)
    return dp[n]

def solution(n):
    return fibo(n)%1234567