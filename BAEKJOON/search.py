## DFS : Depth First Search
## BFS : Breadth First Search


# 1260 DFS와 BFS

from collections import deque

n, m, v = map(int, input().split())
m_list = [list(map(int, input().split())) for _ in range(m)]
# print(m_list)

graph = [[] for _ in range(n + 1)] # 0 이상 n 이하
# print(graph)

for i in range(m):
    graph[m_list[i][0]].append(m_list[i][1])
    graph[m_list[i][1]].append(m_list[i][0])

# for i in range(m):
for i in range(n + 1):
    graph[i].sort()

# print(graph)

visited = [False] * (n + 1)
def dfs(graph, v, visited):
    visited[v] = True           # 현재 노드 방문 처리
    print(v, end = ' ')

    # 현재 노드와 관련된 다른 노드를 '재귀적으로' 방문
    for i in graph[v]:
        if not visited[i]:
            # print(v,"|", end = ' ')         # 출력 처리
            dfs(graph, i, visited)

dfs(graph, v, visited)
print()

visited = [False] * (n + 1)

def bfs(graph, start, visited):
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    print(start, end= ' ')
    while queue: # 큐가 빌 때까지 반복
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                print(i, end= ' ')

bfs(graph, v, visited)