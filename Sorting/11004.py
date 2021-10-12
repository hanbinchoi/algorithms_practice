import sys

n,k = map(int,sys.stdin.readline().split())
numList = list(map(int,sys.stdin.readline().split()))

result = sorted(numList[:n], key=lambda x:x)

print(result[k-1])