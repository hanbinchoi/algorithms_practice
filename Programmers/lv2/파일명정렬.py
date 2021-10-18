import operator


def solution(files):
    answer = []
    fileDict = {}
    for i in range(len(files)):
        head = ""
        number = ""
        tail = ""
        startNumber = False
        startTail = False
        for j in files[i]:
            if not j.isdigit() and not startNumber and not startTail:
                head += j
            elif j.isdigit() and not startTail:
                startNumber = True
                number += j
            else:
                startTail = True
                tail += j
        fileDict[i] = [head,number,tail]
    print(fileDict)
    fileDict = sorted(fileDict.items(), key=lambda x:(x[1][0].lower(),int(x[1][1])))
    answer = []
    for i in fileDict:
        answer.append(i[1][0]+i[1][1]+i[1][2])
    return answer
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))