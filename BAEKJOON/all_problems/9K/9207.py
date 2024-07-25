# 2024.07.25 10:41 ~ 11:27

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e7))

def btr(board, pins, inc_xy, X, Y, left_pins_cnt, move_cnt):
    global ans
    if ans[0] >= left_pins_cnt:
        if ans[0] == left_pins_cnt:
            if ans[1] > move_cnt:
                ans[1] = move_cnt
        else:
            ans = [left_pins_cnt, move_cnt]

    for px, py in pins:
        for ix, iy in inc_xy:
            nx, ny = px+ix, py+iy
            nnx, nny = nx+ix, ny+iy

            if (0 <= nnx < X) and (0 <= nny < Y):
                removal_pin, new_locate_pin = tuple([nx, ny]), tuple([nnx, nny])
                if (removal_pin in pins) and (new_locate_pin not in pins) and (board[nnx][nny] != '#'):
                    new_pins = pins.copy()
                    new_pins.remove(tuple([px, py]))
                    new_pins.remove(removal_pin)
                    new_pins.add(new_locate_pin)
                    btr(board, new_pins, inc_xy, X, Y, left_pins_cnt-1, move_cnt+1)

def solve():
    inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for _ in range(int(input())):
        # board 초기화
        board = []
        line = input().rstrip()
        while line:
            board.append(line)
            line = input().rstrip()

        X, Y = len(board), len(board[0])
        pins = set([tuple([x,y]) for x in range(X) for y in range(Y) if board[x][y] == 'o'])

        global ans
        ans = [9, 0]

        btr(board, pins, inc_xy, X, Y, len(pins), 0)
        print(*ans)

solve()