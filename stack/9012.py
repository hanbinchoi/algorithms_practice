import sys

N = int(sys.stdin.readline())

for _ in range(N):
    data = input()
    psCount = 0
    stack = []
    if len((data))%2 == 0:
        for i in range(len(data)):
            if data[i]=='(':
                stack.append(data[i])
            elif data[i]==')':
                if len(stack) == 0:
                    break
                if stack[-1]=='(':
                    stack.pop()
                    psCount += 1
                else:
                    break
        if psCount == len(data)//2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")