def recursive_function(i):
    print(i,"재귀함수를 호출합니다.")
    i += 1
    if i == 100: return
    recursive_function(i)

recursive_function(0)