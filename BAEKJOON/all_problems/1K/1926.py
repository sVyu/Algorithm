import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
q = deque()
space_cnt, max_area = 0, 0

for x in range(n):
    for y in range(m):
        if board[x][y] == 1 and not visited[x][y]:
            q.append([x, y])
            visited[x][y] = True
            space_cnt += 1
            area = 1

            while(q):
                tx, ty = q.popleft()
                for px, py in inc_xy:
                    nx, ny = tx+px, ty+py
                    if(0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and not visited[nx][ny]):
                        q.append([nx, ny])
                        visited[nx][ny] = True
                        area += 1
            max_area = max(max_area, area)

print(space_cnt)
print(max_area)