N, L, D = map(int, input().split())

limit = 4000
music_on = [False]*limit
for n in range(N):
    for l in range(L):
        music_on[(L+5)*n+l] = True

for d in range(D, limit, D):
    if not music_on[d]:
        print(d)
        break