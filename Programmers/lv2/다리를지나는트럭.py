def solution(bridge_length, weight, truck_weights):
    answer = 0
    sec = 0
    while True:
        if len(truck_weights) == 0:
            break
        n = 0
        end = []
        for i in range(bridge_length):
            if n+truck_weights[0]>weight:
                break
            end.append(truck_weights[0])
            n += truck_weights.pop(0)

            if len(truck_weights) == 0:
                break
        sec += bridge_length * len(end)

    return sec

print(solution(100,100, [10]))