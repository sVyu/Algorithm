N, H, W = map(int, input().split())

target = ['?']*N
for arr in [list(input()) for _ in range(H)]:
    for i in range(N*W):
        if arr[i] != '?':
            target[i//W] = arr[i]

print(''.join(target))