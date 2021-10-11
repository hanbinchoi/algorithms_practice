t = int(input())
for i in range(t):
    try:
        a, b = map(int, input().split())
        print("Case #",i+1,": ",a," + ",b," = ",a+b, sep="")
    except:
        break