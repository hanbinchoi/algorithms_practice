def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return answer

print(solution(["934793", "44", "34", "9347"] ))

# 소팅: 소팅하면 전두사가 전체 번호 앞에 소팅됨 -> 전두사를 앞에 번호가 포함하면 false로 리턴