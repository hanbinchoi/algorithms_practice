def solution(numbers, hand):
    answer = ''
    keypad = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        "*": [3, 0], 0: [3, 1], "#": [3, 2],
    }
    left = "*"
    right = "#"

    for key in numbers:
        if key in [1, 4, 7, "*"]:
            answer += "L"
            left = key
        elif key in [3, 6, 9, "#"]:
            answer += "R"
            right = key
        else:
            x,y = keypad[key][0],keypad[key][1] # 2 1
            lx, ly = keypad[left][0],keypad[left][1] # 2 0
            rx, ry = keypad[right][0],keypad[right][1] # 3 1
            left_distance = abs(x - lx) + abs(y - ly)
            right_distance = abs(x - rx) + abs(y - ry)
            print(key, left, right)
            print(left_distance, right_distance)
            if left_distance > right_distance:
                answer += "R"
                right = key
            elif left_distance < right_distance:
                answer += "L"
                left = key
            else:
                if hand == "left":
                    answer += "L"
                    left = key
                else:
                    answer += "R"
                    right = key
    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))