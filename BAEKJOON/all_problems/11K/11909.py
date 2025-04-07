import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    # print(board)

    INF = int(1e7)
    dp = [[INF]*n for _ in range(n)]
    dp[0][0] = 0

    inc_xy = [[0, 1], [1, 0]]
    for x in range(n):
        for y in range(n):
            for px, py in inc_xy:
                nx, ny = x+px, y+py
                if((nx >= n) | (ny >= n)): continue
                # print(nx, ny)
                dp[nx][ny] = min(dp[nx][ny], dp[x][y] + max(0, board[nx][ny]-board[x][y]+1))

    print(dp[n-1][n-1])

solve()


# import sys
# input = sys.stdin.readline
# from heapq import heappush, heappop

# def solve():
#     n = int(input())
#     board = [list(map(int, input().split())) for _ in range(n)]
#     # print(board)

#     INF = int(1e7)
#     dists = [[INF]*n for _ in range(n)]
#     # print(dists)

#     inc_xy = [[0, 1], [1, 0]]
#     dists[0][0] = True

#     heap = [[0, 0, 0]]
#     while(heap):
#         dist, x, y = heappop(heap)
#         if(dists[x][y] < dist): continue
#         # dists[x][y] = dist

#         for px, py in inc_xy:
#             nx, ny = x+px, y+py
#             if((nx < 0) | (nx >= n) | (ny < 0) | (ny >= n)): continue

#             new_dist = dist+max(0, (board[nx][ny]+1) - board[x][y])
#             if(dists[nx][ny] > new_dist):
#                 dists[nx][ny] = new_dist
#                 heappush(heap, [new_dist, nx, ny])

#     print(dists[n-1][n-1])

# solve()