# 49189 가장 먼 노드
# from collections import defaultdict, deque
# def solution(n, edge):
#     g = defaultdict(list)
#     for a, b in edge:
#         g[a].append(b)
#         g[b].append(a)

#     que = deque([[1, 0]])
#     d = [0] * (n+1) 
#     visited = [False] * (n+1)
#     visited[1] = True

#     while que:
#         v, cnt = que.popleft()
#         d[v] = cnt
#         for u in g[v]:
#             if not visited[u]:
#                 visited[u] = True
#                 que.append([u, cnt+1])

#     max_d = max(d)
#     # print(max_d)
#     return sum([1 for val in d if val == max_d])

# print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))


# 단어 변환
# from collections import deque
# def solution(begin, target, words):
#     que = deque([[begin, 0]])
#     len_word = len(begin)

#     made_word = set()
#     made_word.add(begin)

#     while que:
#         this_word, ans = que.popleft()
#         for w in words:
#             cnt = 0
#             for i in range(len_word):
#                 if this_word[i] != w[i]:
#                     cnt += 1

#                 if cnt >= 2:
#                     break

#             if cnt == 1:
#                 if w == target:
#                     return ans + 1
#                 if w not in made_word:
#                     made_word.add(w)
#                     que.append([w, ans +1])
#     return 0

# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))


# 여행 경로
# from collections import defaultdict

# def dfs(g, now_route:list, cnt, n, check):
#     for next_v in g[now_route[-1]]:
#         if check[(now_route[-1]), next_v] > 0:
#             check[(now_route[-1]), next_v] -= 1
#             # print(check)
#             next_route = now_route + [next_v]
#             # print(next_route)
#             if cnt == n:
#                 return next_route
#             else:
#                 ans = dfs(g, next_route, cnt+1, n, check)
#                 if ans != None:
#                     return ans
#                 check[(now_route[-1]), next_v] += 1

# def solution(tickets):
#     g = defaultdict(list)
#     check = defaultdict(int)
#     for t in tickets:
#         g[t[0]].append(t[1])
#         check[(t[0], t[1])]+= 1
#     # print(g)

#     for key, val in g.items():
#         g[key] = sorted(val)
#     # print(g)

#     return dfs(g, ["ICN"], 1, len(tickets), check)

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))


