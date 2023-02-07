# K번째수
# def solution(array, commands):
#     answer = []

#     for l, r, idx in commands:
#         # print(l, r, idx)
#         answer.append(sorted(array[l-1:r])[idx-1])

#     return answer

# print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))


# H-Index
# pm 03:26

# 0 1 3 5 6
# 0 1 4 5 6
# def solution(citations):
#     cit = sorted(citations)
#     len_cit = len(cit)

#     idx = 0
#     max_h = 0
#     for h in range(0, cit[-1]+1):
#         while idx+1 < len_cit and cit[idx+1] < h:
#             idx += 1
#         # print(h, idx)

#         upper_h = len_cit - idx
#         if idx != 0:
#             upper_h -= 1

#         if upper_h >= h:
#             # max_h = max(max_h, h)
#             max_h = h

#     return max_h

'''
5 5 5 5 5
5
'''
''' 결정적인 반례 !
1 3 3
2
'''

# def solution(citations):
#     cit = sorted(citations)
#     len_cit = len(cit)

#     idx, max_h = -1, 0
#     for h in range(0, cit[-1]+1):
#         while idx+1 < len_cit and cit[idx+1] < h:
#             idx += 1
#         # print(h, idx)

#         # upper_h : h번 이상 인용된 논문 수
#         upper_h = len_cit - (idx+1)

#         if upper_h >= h:
#             max_h = h

#     return max_h
# print(solution([3, 0, 6, 1, 5]))
# print(solution(list(map(int, input().split()))))

# def solution(citations):
#     cit = sorted(citations)
#     len_cit = len(cit)

#     for idx in range(len_cit):
#         if cit[idx] >= len_cit-idx:
#             return len_cit-idx
#     return 0

# print(solution([0]))
# print(solution([0, 0, 2]))