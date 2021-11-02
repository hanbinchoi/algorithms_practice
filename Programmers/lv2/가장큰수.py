def solution(num):
    num = list(map(str, num))
    num.sort(key = lambda x : x*3, reverse = True)
    return str(int(''.join(num)))

print(solution([3, 30, 34, 5, 9]))

# x*3 을 하면 x가 string이므로 '3' -> 333, '30' -> '303030' 이런식으로 변환, 이걸 역순 소팅