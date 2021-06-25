def trapping_rain(buildings):
    # 코드를 작성하세요
    total = 0
    for i in range(1, len(buildings) - 1):
        max_left = max(buildings[:i])
        max_right = max(buildings[i:])

        upper_bound = min(max_left, max_right)
        print("upper",upper_bound)
        total += max(0, upper_bound - buildings[i])
    return total


print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))