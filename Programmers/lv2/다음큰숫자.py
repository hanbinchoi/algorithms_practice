def solution(n):
    answer = 0
    check = bin(n)
    check = str(check)[2:]
    check = check.count("1")
    while True:
        n += 1
        if check == str(bin(n))[2:].count("1"):
            break
    return n

print(solution(78))