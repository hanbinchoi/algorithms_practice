n = int(input())
a = [int(x) for x in input().split()]
a = a[:n]
a.sort()
print(a)
answer = 0
wait = 0
for i in a:
    answer += i+wait
    wait += i
print(answer)