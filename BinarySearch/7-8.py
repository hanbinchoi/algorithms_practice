# n,m = map(int,input().split())
#
# data = list(map(int,input().split()))
# data = data[:n]
#
# data.sort()

# cut = sum(data) // n
#
# new_data = []
# for i in range(len(data)):
#     if(data[i]>cut):
#         new_data.append(data[i])
#
# answer = (sum(new_data)-m) // len(new_data)
#
# print(answer)

# def binary_search(data,target,start,end):
#
#     while(start<=end):
#         mid = (start+end) // 2
#         answer = 0
#
#         for i in range(len(data)):
#             if data[i]>mid:
#                 answer+= data[i]-mid
#
#         if answer == target: return mid
#
#         elif answer> target:
#             start = mid+1
#         elif answer < target:
#             end = mid-1
#
#
# print(binary_search(data,m,0,max(data)))
#
# n,m = map(int,input().split())
#
# data = list(map(int,input().split()))
# data = data[:n]
#
# def binary_search(data,target,start,end):
#     while(start<=end):
#         mid = (start+end) // 2
#         result = 0
#
#         for i in range(len(data)):
#             if data[i]>mid:
#                 result += data[i]-mid
#
#         if result == target: return mid
#
#         elif result > target:
#             start = mid+1
#         elif result < target:
#             end = mid-1
#
# print(binary_search(data,m,0,data[n-1]))

n, m = map(int,input().split())
data = list(map(int,input().split()))
data = data[:n]
data.sort()

def binary_search(data,target,start,end):

    while start<=end:
        mid = (start+end) //2
        result = 0
        for i in range(len(data)):
            if (data[i]-mid) > 0:
                result += data[i]-mid

        print(start, end, mid, result)

        if result == target: return mid

        elif result > target: start=mid+1

        elif result < target: end= mid-1


    return None

print(binary_search(data,m,0,data[n-1]))