n,k = map(int,input().split())

A = []
B = []

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A = A[:n]
B = B[:n]
#
# for i in range(k):
#     a = min(A)
#     b = max(B)
#
#     if a<b:
#         a_index = A.index(a)
#         b_index = B.index(b)
#         A.pop(a_index)
#         B.pop(b_index)
#         A.append(b)
#         B.append(a)
#
#
A.sort()
B.sort(reverse=True)

for i in range(k):
    if A[i]<B[i]:
        A[i], B[i] = B[i], A[i]
        
print(sum(A))
