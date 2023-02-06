# from collections import deque
# def solution(numbers, target):
#     len_numbers = len(numbers)
#     # visited = [False] * len_numbers
#     # visited[0] = True
#     ans = 0

#     que = deque([[0, numbers[0]], [0, -numbers[0]]])
#     # que.append()

#     while que:
#         v, val = que.popleft()
#         # print(v, val)

#         if v+1 < len_numbers:
#             que.append([v+1, val+numbers[v+1]])
#             que.append([v+1, val-numbers[v+1]])
#         else:
#             if val == target:
#                 ans += 1

#     return ans

# solution([1, 1, 1, 1, 1], 3)


# 게임 맵 최단거리
# BFS
# from collections import deque
# def solution(maps):
#     answer = -1
    
#     n, m = len(maps), len(maps[0])
#     # print(n, m)

#     visited = [[False]*m for _ in range(n)]
#     visited[0][0] = True

#     que = deque()
#     que.append([0, 0, 1])

#     inc_xy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

#     pos = False
#     while que:
#         x, y, cnt = que.popleft()
#         for px, py in inc_xy:
#             nx, ny = x + px, y + py
#             if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
#                 if nx == n-1 and ny == m-1:
#                     answer = cnt+1
#                     pos = True
#                     break
#                 visited[nx][ny] = True
#                 que.append([nx, ny, cnt+1])
#         if pos:
#             break
#         # print(que)

#     return answer

# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))


# 여행경로
# 음 ~