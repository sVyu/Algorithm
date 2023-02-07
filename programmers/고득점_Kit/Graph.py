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

