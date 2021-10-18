def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
                break
            else:
                stack.pop(len(stack)-1)

    return True if len(stack)==0 else False

print(solution("(())()"))
