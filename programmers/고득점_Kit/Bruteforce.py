# 전력망을 둘로 나누기
# from collections import defaultdict, deque
# def solution(n, wires):
#     answer = n

#     g = defaultdict(list)
#     for u, v in wires:
#         g[u].append(v)
#         g[v].append(u)

#     for std_u, std_v in wires:
#         g[u].remove(v)
#         g[v].remove(u)

#         que = deque()
#         que.append(1)
#         visited = [False] * (n+1)
#         visited[1] = True
#         cnt = 1

#         while que:
#             now_v = que.popleft()
#             # print(now_v)
#             for next_u in g[now_v]:
#                 # if now_v in [std_v, std_u] and u in [std_v, std_u]:
#                 #     continue

#                 if next_u != std_u and not visited[next_u]:
#                     cnt += 1
#                     visited[next_u] = True
#                     que.append(next_u)

#         answer = min(answer, abs(cnt-(n-cnt)))
#         print(std_u, std_v, answer)

#         g[u].append(v)
#         g[v].append(u)

#     return answer

# print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
# print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
# print(solution(8, [[1,2], [2,3], [3, 4], [1, 5], [1, 6],[5, 7], [6, 8]])) # this_case

# clear
# from collections import defaultdict, deque
# def solution(n, wires):
#     answer = n

#     g = defaultdict(list)
#     for u, v in wires:
#         g[u].append(v)
#         g[v].append(u)

#     for std_u, std_v in wires:
#         que = deque()
#         que.append(std_v)
#         visited = [False] * (n+1)
#         visited[std_v] = True
#         cnt = 1

#         while que:
#             now_v = que.popleft()
#             for next_u in g[now_v]:
#                 if next_u != std_u and not visited[next_u]:
#                     cnt += 1
#                     visited[next_u] = True
#                     que.append(next_u)

#         answer = min(answer, abs(cnt-(n-cnt)))

#     return answer

# print(solution(8, [[1,2], [2,3], [3, 4], [1, 5], [1, 6],[5, 7], [6, 8]]))


# 모의고사
# def solution(answers):
#     answer = []

#     w = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
#     len_w = [len(w[0]), len(w[1]), len(w[2])]
#     cnt_w = [0, 0, 0]
#     p = [0, 0, 0]

#     for a in answers:
#         for idx in range(3):
#             if w[idx][p[idx]] == a:
#                 cnt_w[idx] += 1
#             p[idx] = (p[idx]+1) % len_w[idx]
#         # print(p)
#     # print(cnt_w)

#     max_val = max(cnt_w)
#     for idx in range(3):
#         if cnt_w[idx] == max_val:
#             answer.append(idx+1)

#     return answer

# print(solution([1,2,3,4,5]))
# print(solution([1,3,2,4,2]))


# 소수 찾기
# import itertools
# def solution(numbers):
#     answer = 0
#     len_numbers = len(numbers)

#     sieves = [False, False] + [True]*(10**len_numbers)
#     for k in range(2, len(sieves)):
#         if sieves[k]:
#             for kk in range(2*k, len(sieves), k):
#                 sieves[kk] = False

#     num_set = set()
#     for num_len in range(1, len_numbers+1):
#         for ns in itertools.permutations([i for i in range(len_numbers)], num_len):
#             # print(ns)
#             this_n = int("".join(numbers[n] for n in ns))
#             # print(this_n)
#             if sieves[this_n] and this_n not in num_set:
#                 num_set.add(this_n)
#                 answer += 1

#     return answer

# print(solution("17"))
# print(solution("011"))
# print(solution("1234567"))


# 최소직사각형
# def solution(sizes):
#     w, h = 0, 0
#     for s in sizes:
#         s = sorted(s)
#         w = max(w, s[0])
#         h = max(h, s[1])

#     return w * h

# print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))