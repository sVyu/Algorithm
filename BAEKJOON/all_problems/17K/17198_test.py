from collections import deque

def sol1(board):
    # board = [list(input()) for _ in range(10)]
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
                    # print(cnt)
                    return cnt
                    # exit()

def sol2(board):
    # board = [list(input()) for _ in range(10)]
    b, r, l = [], [], []

    for x in range(10):
        for y in range(10):
            if board[x][y] == 'B':
                b = [x, y]
            elif board[x][y] == 'R':
                r = [x, y]
            elif board[x][y] == 'L':
                l = [x, y]

    if (b[0] == l[0]) and ((b[1] < r[1] < l[1]) or (b[1] > r[1] > l[1])):
        return abs(b[1]-l[1]+1)
    elif (b[1] == l[1]) and ((b[0] < r[0] < l[0]) or (b[0] > r[0] > l[0])):
        return abs(b[0]-l[0]+1)
    else:
        return abs(b[0]-l[0])+abs(b[1]-l[1])-1

def test():
    check = [False]*100

    for val1 in range(100):
        if check[val1]: continue
        check[val1] = True
        x1, y1 = val1//10, val1%10

        for val2 in range(100):
            if check[val2]: continue
            check[val2] = True
            x2, y2 = val2//10, val2%10

            for val3 in range(100):
                if check[val3]: continue
                check[val3] = True
                x3, y3 = val3//10, val3%10

                board = [['.']*10 for _ in range(10)]
                board[x1][y1] = 'B'
                board[x2][y2] = 'R'
                board[x3][y3] = 'L'

                sol1_val, sol2_val = sol1(board), sol2(board)
                if sol1_val != sol2_val:
                    for k in range(10):
                        print(board[k])

                    print("diff")
                    print(sol1_val, sol2_val)
                    input()

                check[val3] = False
            check[val2] = False
        check[val1] = False

test()