dayIndex = ["MON","TUE","WED","THU","FRI","SAT","SUN"]

monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]

month, day = map(int,(input().split()))

totalDay = day-1
afterMonth = month-1

for i in range(afterMonth):
    totalDay += monthDays[i]

print(dayIndex[totalDay%7])
