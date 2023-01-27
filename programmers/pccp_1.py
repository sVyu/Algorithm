# 2023/01/27
# pm 04:04 ~ 04:22

# 1
# def solution(input_string):
#     alone_alpha = [0] * 26
#     pre_a = ''

#     # from string import ascii_lowercase
#     # lowercase = list(ascii_lowercase)
#     # # print(lowercase)

#     # 체크
#     for a in input_string:
#         # 연속 되어있지 않음
#         if a != pre_a:
#             ord_val = ord(a)-97
#             # 외톨이 알파벳
#             if alone_alpha[ord_val] == 0:
#                 alone_alpha[ord_val] = 1
#             else:
#                 alone_alpha[ord_val] = -1

#         pre_a = a

#     # 정답 string
#     ans = ""
#     for idx in range(26):
#         if alone_alpha[idx] == -1:
#             ans += f'{chr(97+idx)}'

#     return ans if ans != "" else "N"
#     # print(ans if ans != "" else "N")

# solution("zbzbz")


# ~ 04:32
# 2
# def solution(ability):
#     answer = 0

#     import itertools
#     for idxs in itertools.permutations([i for i in range(len(ability))], len(ability[0])):
#         # print(idx)
#         now_sum = 0
#         sub_idx = 0
#         for idx in idxs:
#             now_sum += ability[idx][sub_idx]
#             sub_idx += 1
#         answer = max(answer, now_sum)

#     return answer


# 3
# pm 05:17 ~ 47

# def recursion(depth, idx):
#     if depth == 1:
#         return "Rr"
#     elif depth == 2:
#         gen = ["RR", "Rr", "Rr", "rr"]
#         return gen[idx]
#     else: # depth >= 3
#         total_idxs = 4**(depth-1)
#         quarter_idxs = total_idxs // 4

#         if idx < quarter_idxs:
#             return "RR"
#         elif idx < 3 * quarter_idxs:
#             return recursion(depth-1, idx % quarter_idxs)
#         else:
#             return "rr"

# def solution(queries):
#     answer = []
#     for depth, idx in queries:
#         answer.append(recursion(depth, idx-1))

#     return answer

# # print(solution([[3, 1], [2, 3], [3, 9]]))
# # print(solution([[4, 26]]))


# 4  05:48 ~ 06:40
# 문제를 완전하게 이해하고 푸는 게 시간 단축의 지름길

# from heapq import heappush, heappop
# def solution(program):
#     answer = [0]*11

#     heap1, heap2 = [], []
#     now_time = 0

#     for p in program:
#         heappush(heap2, [p[1], p[0], p[2]])
#     # print(heap2)

#     for _ in range(len(program)):
#         while heap2 and (heap2[0][0] <= now_time or not heap1):
#             p = heappop(heap2)
#             heappush(heap1, [p[1], p[0], p[2]])

#         grade, called_time, running_time = heappop(heap1)
#         if now_time > called_time:
#             answer[grade] += now_time - called_time
#         else:
#             now_time = called_time

#         now_time += running_time

#     answer[0] = now_time
#     return answer

# print(solution([[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]))
# print(solution([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]))
# 오류 발생 예시
# print(solution([[2, 0, 10], [1, 15, 5]]))