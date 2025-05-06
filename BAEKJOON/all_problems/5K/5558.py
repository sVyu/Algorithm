import sys
input = sys.stdin.readline
from collections import deque

def solve():
    h, w, cheese_cnt = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(h)]
    # print(board)

    sxy = []
    for x in range(h):
        for y in range(w):
            if(board[x][y] == 'S'):
                sxy = [x, y]
    # print(sxy)
    inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    ans = 0
    q = deque([tuple([sxy[0], sxy[1]])])

    for cc in range(1, cheese_cnt+1):
        move_cnt = 0
        visited = [[False]*w for _ in range(h)]
        next_sxy = []

        while(q):
            move_cnt += 1
            len_q = len(q)
            for _ in range(len_q):
                sx, sy = q.popleft()
                for px, py in inc_xy:
                    nx, ny = sx+px, sy+py
                    if((nx < 0) | (nx >= h) | (ny < 0) | (ny >= w)):
                        continue
                    if(visited[nx][ny] | (board[nx][ny] == 'X')):
                        continue

                    visited[nx][ny] = True
                    if(board[nx][ny] == str(cc)): #
                        board[nx][ny] = '.' #
                        ans += move_cnt
                        next_sxy = [nx, ny]
                        q.clear()
                        break
                    else:
                        q.append(tuple([nx, ny]))

                if(not q): break

        q.append(tuple(next_sxy))

    print(ans)

solve()