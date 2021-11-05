from itertools import combinations, permutations

n= input()

nlist = list(n)
nlist.sort(reverse=True)
num = int(''.join(nlist))
if num%30 == 0:
    print(num)
else:
    print(-1)

