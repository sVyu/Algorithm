import sys
input = sys.stdin.readline
from collections import deque

def solve():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    # print(board)
    inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    ans_dist = -1
    ans_val = -1

    for x in range(n):
        for y in range(m):
            if(board[x][y] == 0): continue

            q = deque([[x, y]])
            tmp_dist = -1
            tmp_val = -1
            visited = [[False]*m for _ in range(n)]
            visited[x][y] = True

            while(q):
                tmp_dist += 1
                len_q = len(q)
                for _ in range(len_q):
                    bx, by = q.popleft()
                    tmp_val = board[x][y]+board[bx][by]

                    if(ans_dist < tmp_dist):
                        ans_dist = tmp_dist
                        ans_val = tmp_val
                    elif(ans_dist == tmp_dist):
                        if(ans_val < tmp_val):
                            ans_val = tmp_val

                    for px, py in inc_xy:
                        nx, ny = bx+px, by+py
                        if((nx<0)|(nx>=n)|(ny<0)|(ny>=m)): continue
                        if(board[nx][ny]==0): continue
                        if(visited[nx][ny]): continue

                        visited[nx][ny] = True
                        q.append([nx, ny])

    print(ans_val)

solve()