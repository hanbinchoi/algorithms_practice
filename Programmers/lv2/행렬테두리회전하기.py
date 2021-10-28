import copy


def solution(rows, columns, queries):
    answer = []
    matrix = [[(i+1)+(rows*j) for i in range(columns)] for j in range(rows)]


    for query in queries:
        temp_matrix = copy.deepcopy(matrix)
        rotate = []
        for i in range(query[0]-1,query[2]):
            for j in range(query[1]-1, query[3]):
                if i == query[0]-1 or i == query[2]-1 or j == query[1]-1 or j == query[3]-1:
                    if i == query[0]-1 and j != query[1]-1:  #첫번째 열 첫번째 행 아니면
                        matrix[i][j] = temp_matrix[i][j-1]
                    elif j == query[3]-1 : #마지막 행 이고 마지막 열 아니면
                        matrix[i][j] = temp_matrix[i-1][j]
                    elif i == query[2]-1 : # 마지막 열 이고 첫번째 행 아니면
                        matrix[i][j] = temp_matrix[i][j+1]
                    elif j == query[1]-1:
                        matrix[i][j] = temp_matrix[i+1][j]
                    rotate.append(matrix[i][j])

        answer.append(min(rotate))
        rotate.clear()
    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))