def solution(nums):
    answer = 0
    choice = len(nums)//2
    pokemonNum = {}
    for i in set(nums):
        pokemonNum[i] = 0

    for i in nums:
        pokemonNum[i] += 1

    print(len(pokemonNum))
    if len(pokemonNum) > choice:
        answer = choice
    else:
        answer = len(pokemonNum)
    return answer

print(solution([3,1,2,3]))