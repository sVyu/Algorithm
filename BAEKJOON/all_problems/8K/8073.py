import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
# print(board)

ans = []
for i in range(N-1):
    for j in range(i+1, N):
        shortest_way = True
        for k in range(N):
            if k in [i, j]: continue
            if board[i][j] >= (board[i][k]+board[k][j]):
                shortest_way = False
                break

        if shortest_way:
            ans.append([i+1, j+1])

for a in sorted(ans):
    print(*a)