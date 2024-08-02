import sys
input = sys.stdin.readline

def btr(board, x, y, move_cnt, eat_cnt, inc_xy):
    backuped_cell = board[x][y]
    board[x][y] = -1
    for px, py in inc_xy:
        nx, ny = x+px, y+py
        if 0 <= nx < 5 and 0 <= ny < 5 and board[nx][ny] != -1:
            if move_cnt < 3:
                new_eat_cnt = eat_cnt + board[nx][ny]
                if new_eat_cnt >= 2:
                    return True
                if btr(board, nx, ny, move_cnt+1, new_eat_cnt, inc_xy):
                    return True

    board[x][y] = backuped_cell
    return False

def solve():
    board = [list(map(int, input().split())) for _ in range(5)]
    x, y = map(int, input().split())
    inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    print(1 if btr(board, x, y, 0, board[x][y], inc_xy) else 0)

solve()

