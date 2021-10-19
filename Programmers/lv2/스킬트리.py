def solution(skill, skill_trees):
    answer = len(skill_trees)
    for i in skill_trees:
        order = []
        for j in skill:
            order.append(i.find(j))

        if order[0] == -1:
            if order.count(-1) == len(order):
                continue
            else:
                print(order)
                answer -= 1
                continue

        for k in range(len(order)-1):
            if order[k+1] == -1 and k+1 != len(order)-1:
                print(order)
                pass
            elif k+1 == len(order)-1 and order[k+1] == -1:
                break
            elif order[k] >= order[k+1]:
                print(order)
                answer -= 1
                break
    return answer

print(solution("CBDK", ["CB", "CXYB", "BD", "AECD", "ABC", "AEX", "CDB", "CBKD", "IJCB", "LMDK"]))