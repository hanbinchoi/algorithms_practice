# n,m = map(int,input().split())
# a,b,d = map(int,input().split())
#
# field = list()
#
# direction = [0,1,2,3]
# step = [(-1,0),(0,1),(1,0),(0,-1)]
# count = 0
# check = 0
# isBack = False
#
# for i in range(n):
#     field.append(list(map(int,input().split())))
#
# while(True):
#     # 0이면 카운트 +1, 1로 체크
#     if(field[a][b] == 0):
#         count += 1
#         field[a][b] = 1
#         isBack = False
#         a = a + step[direction[d]][0]
#         b = b + step[direction[d]][1]
#     # 1이면
#     # 1. 현재 방향을 기준으로 왼쪽방향 탐색
#     # 2. 1이면 다시 왼쪽 회전
#     # 3. 모든 방향이 1이면 보는 방향을 기준으로 한칸 뒤로 돌아가고 1단계로 돌아가고 뒤가 1이면 움직임 멈춤
#     elif isBack and field[a][b] ==1:
#         break
#     else:
#         if d==0:
#             d=3
#         else: d -= 1
#
#         if(check!=4):
#             na = a + step[direction[d]][0]
#             nb = b + step[direction[d]][1]
#
#             check += 1
#             if(field[na][nb] == 1):
#                 continue
#             else:
#                 a=na
#                 b=nb
#                 check=0
#         else:
#             na = a - step[direction[d]][0]
#             nb = b - step[direction[d]][1]
#             isBack = True
#
# print(count)


# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1  # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)