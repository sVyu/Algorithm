import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
board = [list(input().rstrip()) for _ in range(N)]

max_cnt = int(1e4)
cnts = [[max_cnt]*N for _ in range(N)]
inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# x, y, d(direction), direction_changed_cnt
q = deque([[0, 0, -1, 0]])
# cnts[0][0] = 0

while q:
    x, y, pre_d, cnt = q.popleft()
    for d in range(4):
        px, py = inc_xy[d]
        nx, ny = x+px, y+py
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == '.':
            new_cnt = cnt + (1 if d != pre_d else 0)
            if cnts[nx][ny] >= new_cnt: # 
                cnts[nx][ny] = new_cnt
                q.append([nx, ny, d, new_cnt])

print(cnts[N-1][N-1])

# for x in range(N):
#     print(cnts[x])