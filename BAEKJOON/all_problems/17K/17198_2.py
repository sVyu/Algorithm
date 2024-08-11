board = [list(input()) for _ in range(10)]
b, r, l = [], [], []

for x in range(10):
    for y in range(10):
        if board[x][y] == 'B':
            b = [x, y]
        elif board[x][y] == 'R':
            r = [x, y]
        elif board[x][y] == 'L':
            l = [x, y]

if (b[0] == r[0] == l[0]) and ((b[1] < r[1] < l[1]) or (b[1] > r[1] > l[1])):
    print(abs(b[1]-l[1])+1)
elif (b[1] == r[1] == l[1]) and ((b[0] < r[0] < l[0]) or (b[0] > r[0] > l[0])):
    print(abs(b[0]-l[0])+1)
else:
    print(abs(b[0]-l[0])+abs(b[1]-l[1])-1)