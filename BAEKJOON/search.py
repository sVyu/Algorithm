## DFS : Depth First Search
## BFS : Breadth First Search


# 1260 DFS와 BFS
# from collections import deque

# n, m, v = map(int, input().split())
# m_list = [list(map(int, input().split())) for _ in range(m)]
# # print(m_list)

# graph = [[] for _ in range(n + 1)] # 0 이상 n 이하
# # print(graph)

# for i in range(m):
#     graph[m_list[i][0]].append(m_list[i][1])
#     graph[m_list[i][1]].append(m_list[i][0])

# # for i in range(m):
# for i in range(n + 1):
#     graph[i].sort()

# # print(graph)

# visited = [False] * (n + 1)
# def dfs(graph, v, visited):
#     visited[v] = True           # 현재 노드 방문 처리
#     print(v, end = ' ')

#     # 현재 노드와 관련된 다른 노드를 '재귀적으로' 방문
#     for i in graph[v]:
#         if not visited[i]:
#             # print(v,"|", end = ' ')         # 출력 처리
#             dfs(graph, i, visited)

# dfs(graph, v, visited)
# print()

# visited = [False] * (n + 1)
# def bfs(graph, start, visited):
#     queue = deque([start])
#     # 현재 노드를 방문 처리
#     visited[start] = True
#     print(start, end= ' ')
#     while queue: # 큐가 빌 때까지 반복
#         # 큐에서 하나의 원소를 뽑아 출력
#         v = queue.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#                 print(i, end= ' ')

# bfs(graph, v, visited)


# 2178 미로 탐색
# 너비 우선 탐색
# n, m = map(int, input().split())
# maze_list = [list(map(int, input().split())) for _ in range(n)]

# 2606 바이러스

# 10026 적록색약

# import sys
# sys.setrecursionlimit(10**6)
# # recursionlimit

# n = int(input())
# rgb_list = [list(str(input())) for _ in range(n)]
# rgb_check_list = [[0] * n for _ in range(n)]
# case_list = ['R', 'G', 'B', 'RG']
# result_list = [0] * 4


# # 적록색약 아닌 경우
# def dfs(rgb_list, x, y, z):
#     if((x <= -1) | (y <= -1) | (x >= n) | (y >= n)):
#         return False
    
#     if(z == 'RG'):
#         if(rgb_check_list[x][y] == 0) & ((rgb_list[x][y] == 'R') | (rgb_list[x][y] == 'G')):
#             rgb_check_list[x][y] = 1

#             dfs(rgb_list, x-1, y, z)
#             dfs(rgb_list, x, y-1, z)
#             dfs(rgb_list, x+1, y, z)
#             dfs(rgb_list, x, y+1, z)
#             return True

#     elif(rgb_check_list[x][y] == 0) & (rgb_list[x][y] == z):
#         rgb_check_list[x][y] = 1
        
#         # print(rgb_check_list)
#         # os.system("pause")

#         dfs(rgb_list, x-1, y, z)
#         dfs(rgb_list, x, y-1, z)
#         dfs(rgb_list, x+1, y, z)
#         dfs(rgb_list, x, y+1, z)
#         return True
#     return False

# for k in case_list:
#     if(k == 'RG'): # RG
#         rgb_check_list = [[0] * n for _ in range(n)]

#     for i in range(n):      # point index : (i, j)
#         for j in range(n):
#             if(dfs(rgb_list, i, j, k) == True):
#                 # print(i, j)
#                 result_list[case_list.index(k)] += 1

# # print(result_list)
# print(sum(result_list[:3]), sum(result_list[2:]))


# 11403 경로 찾기
# import os
# import copy

# n = int(input())
# route_list = [list(map(int, input().split())) for _ in range(n)]

# # new_route_list = [[0] * n for _ in range(n)]
# # new_route_list = [] + route_list
# # result_route_list = []

# next_route_list = copy.deepcopy(route_list)
# prev_route_list = []

# while next_route_list != prev_route_list :
#     prev_route_list = copy.deepcopy(next_route_list)
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 if((next_route_list[i][j] * route_list[j][k]) == 1):
#                     next_route_list[i][k] = 1
#                     # print(i, j, k, next_route_list)
#                     # os.system("pause")
    
#     # print(prev_route_list)
#     # print(next_route_list)
#     # print()

# for i in range(n):
#     for j in range(n):
#         print(next_route_list[i][j], end= ' ')
#     print()


# 2606 바이러스

# import os

# num_of_com = int(input())
# num_of_pair = int(input())
# pair_list = [list(map(int, input().split())) for _ in range(num_of_pair)]
# # print(pair_list)

# graph = [[] for _ in range(num_of_com + 1)]
# # print(graph)

# for i in range(len(pair_list)):
#     graph[pair_list[i][0]].append(pair_list[i][1])
#     graph[pair_list[i][1]].append(pair_list[i][0])
#     # os.system("pause")
# # print(graph)

# check_list = [False] * (num_of_com+1)
# def check_infected(n) :
#     if(check_list[n] == False):
#         check_list[n] = True
#         for i in graph[n]:
#             check_infected(i)
#             # print(i)

# check_infected(1)
# # print(check_list)
# print(check_list.count(True)-1)


# 14502 연구소
# n, m = map(int, input().split())
# map_list = [list(map(int, input().split())) for _ in range(n)]

# # print(map_list)

# wall_point_list = [[-1, -1] for _ in range(3)]

# zero_point_list = []

# for i in range(n):
#     for j in range(m):
#         if(map_list[i][j] == 0):
#             zero_point_list.append([i, j])
# print(zero_point_list)

# for i in range(len(zero_point_list)):
#     for j in range(i+1, len(zero_point_list)):
#         for k in range(j+1, len(zero_point_list)):
#             wall_point_list[0] = zero_point_list[i]
#             wall_point_list[1] = zero_point_list[j]
#             wall_point_list[2] = zero_point_list[k]

#             print(wall_point_list)
