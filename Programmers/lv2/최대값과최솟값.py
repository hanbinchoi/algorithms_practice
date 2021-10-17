def solution(s):
    numbers = s.split()
    numbers = [int(i) for i in numbers]
    return ""+str(min(numbers))+" "+str(max(numbers))

print(solution("-1 -2 -3 -4"))