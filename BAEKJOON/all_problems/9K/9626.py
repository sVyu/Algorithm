M, N = map(int, input().split())
U, L, R, D = map(int, input().split())

words = [list(input()) for _ in range(M)]
decos = "#."

tot_y = N+L+R
for x in range(M+U+D):
    for y in range(tot_y):
        if U <= x < M+U and L <= y < N+L:
            print(words[x-U][y-L], end='')
        else:
            print(decos[(x+y)%2], end='')
    print()