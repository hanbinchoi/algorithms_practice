def solution(s, n):
    answer = ''
    print(ord('a'), ord('z'))
    print(ord('A'),ord('Z'))
    for i in s:
        if i.isalpha():
            if i.isupper():
                c = ord(i)+n
                if c > 90:
                    c -= 26
            else:
                c = ord(i) + n
                print(c)
                if c > 122:
                    c -= 26
            answer += chr(c)
        else:
            answer += i
    return answer

print(solution("a B z", 4))