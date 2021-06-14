import re
def solution(new_id):
    answer = ''
    id = new_id.lower()
    id_2 = ""
    for i in id:
        if ord(i) >= 97 and ord(i) <= 122: id_2 += i
        elif ord(i) >= 48 and ord(i) <= 57: id_2 += i
        elif ord(i) == 45 or ord(i) == 46 or ord(i) == 95: id_2 += i
    print(id_2)
    id_3 = ""
    k = 0
    for i in id_2:
        if i == '.':
            if k == 0:
                k +=1
                id_3 += i
            else:
                continue
        else:
            id_3 += i
            k = 0
    print(id_3)
    if id_3[0] == '.': id_3 = id_3[1:]
    if id_3[-1] == '.': id_3 = id_3[:-1]
    if id_3 == "": id_3 += 'a'
    print(id_3)
    if len(id_3)>=16: id_3 = id_3[:15]

    if len(id_3) <= 2:
        while True:
            id_3 += id_3[-1]

            if len(id_3) == 3:
                break
    answer = id_3
    return answer




print(solution("z-+.^."))