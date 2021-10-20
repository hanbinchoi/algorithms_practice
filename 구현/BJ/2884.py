hour, minute = map(int,input().split())

minute -= 45

if minute < 0:
    minute = 60 + minute
    hour -= 1

if hour < 0:
    hour = 24 + hour

print(hour,minute)