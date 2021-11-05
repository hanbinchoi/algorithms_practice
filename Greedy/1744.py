n = int(input())

nums = []

for i in range(n):
    nums.append(int(input()))

nums.sort(reverse=True)
positive = [i for i in nums if i>0]
negative = [i for i in nums if i<0]
zero = [i for i in nums if i==0]
ans = 0
while len(positive) >= 2:
    if positive[1] == 1:
        ans += positive[0]+positive[1]
    else:
        ans += positive[0]*positive[1]
    positive.pop(0)
    positive.pop(0)
negative.sort()
while len(negative) >= 2:
    ans += negative[0] * negative[1]
    negative.pop(0)
    negative.pop(0)

while negative:
    if zero:
        ans += 0*negative.pop(0)
        zero.pop()
    else:
        ans += negative.pop(0)

while positive:
    ans += positive.pop(0)

print(ans)