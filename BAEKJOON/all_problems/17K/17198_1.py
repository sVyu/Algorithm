from collections import deque

board = [list(input()) for _ in range(10)]
visited = [[False]*10 for _ in range(10)]
s, e = [], []

for x in range(10):
    for y in range(10):
        if board[x][y] == 'B':
            s = [x, y]
            visited[x][y] = True
        elif board[x][y] == 'L':
            e = [x, y]

q = deque([[*s, 0]])
inc_xy = [[0, 1], [1, 0], [-1, 0], [0, -1]]

while q:
    x, y, cnt = q.popleft()
    for px, py in inc_xy:
        nx, ny = x+px, y+py
        if 0 <= nx < 10 and 0 <= ny < 10 and not visited[nx][ny]:
            if board[nx][ny] == '.':
                visited[nx][ny] = True
                q.append([nx, ny, cnt+1])
            elif board[nx][ny] == 'L':
                visited[nx][ny] = True
                print(cnt)
                exit()