n, t = map(int, input().split())
zs = list(map(int, input().split()))

cnt = 0
val = 0
for z in zs:
    new_val = val+z
    if(new_val <= t):
        cnt += 1
        val = new_val
    else:
        break

print(cnt)