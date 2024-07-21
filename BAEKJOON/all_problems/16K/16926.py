def rot(N, M, board):
    l, r, top, bot = 0, M-1, 0, N-1
    while l < r and top < bot:
        tmp = board[bot][l]
        for x in range(bot, top, -1):
            board[x][l] = board[x-1][l]
        for y in range(l, r):
            board[top][y] = board[top][y+1]
        for x in range(top, bot):
            board[x][r] = board[x+1][r]
        for y in range(r, l, -1):
            board[bot][y] = board[bot][y-1]
        board[bot][l+1] = tmp

        l += 1
        r -= 1
        top += 1
        bot -= 1

def solve():
    N, M, R = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    for _ in range(R):
        rot(N, M, board)

    for x in range(N):
        print(*board[x])

solve()