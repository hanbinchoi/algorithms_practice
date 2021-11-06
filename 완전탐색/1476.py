a,b,c = map(int,input().split())
i = 0
while True:
   i+=1
   if i%15 == a and i%28 == b and i%19 == c:
       print(i)
       break