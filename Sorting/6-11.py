n = int(input())
data =[]
for i in range(n):
    name,score = input().split(' ')
    data.append((name,score))

data.sort(key=lambda data: data[1])
for i in range(len(data)):
    print(data[i][0], end=' ')

# data = sorted(data, key=lambda student: student[1])
#
# for student in data:
#     print(student)