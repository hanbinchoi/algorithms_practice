# x = int(input())
# d = [0] * 30001
#
# # 다이나믹 프로그래밍 진행
# for i in range(2,x+1):
#     # 현재의 수에서 1을 빼는 경우
#     d[i] =d[i-1] +1
#     # 현재의 수가 2로 나누어 떨어지는 경우
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2] + 1)
#     # 현재의 수가 3로 나누어 떨어지는 경우
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)
#     # 현재의 수가 5로 나누어 떨어지는 경우
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i // 5] + 1)
# print(d[:27])

# x = int(input())
#
# d = [0] * 30001
#
# for i in range(2,x+1):
#     # 1을 뺀 케이스
#     d[i] = d[i-1] + 1
#
#     # 2로 나눠지는 케이스
#     if (i % 2 == 0):
#         d[i] = min(d[i], d[i // 2] + 1)
#     # 3로 나눠지는 케이스
#     if (i % 3 == 0):
#         d[i] = min(d[i], d[i // 3] + 1)
#     # 5로 나눠지는 케이스
#     if (i % 5 == 0):
#         d[i] = min(d[i], d[i // 5] + 1)
#
# print(d[x])

x = int(input())

d = [0] * 30001

d[1] = 0

for i in range(2,x+1):
    d[i] = d[i-1]+1

    if (i % 2 == 0):
        d[i] = min(d[i], d[i // 2] + 1)
    if (i % 3 == 0):
        d[i] = min(d[i], d[i // 3] + 1)
    if (i % 5 == 0):
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])