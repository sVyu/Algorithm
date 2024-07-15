N = int(input())
M, K = map(int, input().split())
ns = sorted(list(map(int, input().split())), reverse=True)

now = 0
cnt = 0
target = M*K

for n in ns:
    now += n
    cnt += 1

    if now >= target:
        break

print(cnt if now >= target else "STRESS")