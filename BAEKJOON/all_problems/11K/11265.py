import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    for k in range(N):
        for a in range(N):
            for b in range(N):
                board[a][b] = min(board[a][b], board[a][k]+board[k][b])

    for _ in range(M):
        A, B, C = map(int, input().split())
        A -=1; B-=1
        print("Enjoy other party" if board[A][B] <= C else "Stay here")

solve()