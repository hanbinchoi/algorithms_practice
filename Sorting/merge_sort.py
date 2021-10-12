array = [-1,3,2,4,-1]

def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left,right)

def merge(left, right):
    result = []
    print("--")
    print(left,right)
    print("--")
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                result.append(right[0])
                right = right[1:]
            else:
                result.append(left[0])
                left = left[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
        print(result)
    return result;
print(merge_sort(array))