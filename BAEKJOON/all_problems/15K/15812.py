N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

INF = 21
ans = INF
min_x, max_x = INF, -1
min_y, max_y = INF, -1

towns = [[x, y] for x in range(N) for y in range(M) if board[x][y] == 1]
# print(towns)

board_size = N*M
for dot1 in range(board_size-1):
    x1 = dot1//M
    y1 = dot1-x1*M
    if board[x1][y1] == 1: continue

    for dot2 in range(dot1+1, board_size):
        x2 = dot2//M
        y2 = dot2-x2*M
        if board[x2][y2] == 1: continue

        dist = 0
        for tx, ty in towns:
            dist = max(dist, min(abs(tx-x1)+abs(ty-y1), abs(tx-x2)+abs(ty-y2)))
        ans = min(ans, dist)

print(ans)