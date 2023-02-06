# K번째수
# def solution(array, commands):
#     answer = []

#     for l, r, idx in commands:
#         # print(l, r, idx)
#         answer.append(sorted(array[l-1:r])[idx-1])

#     return answer

# print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))