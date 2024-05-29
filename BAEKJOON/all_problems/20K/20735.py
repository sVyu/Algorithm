cnt = 0
for _ in range(int(input())):
    ss = input().lower()
    for t in ["pink", "rose"]:
        if t in ss:
            cnt += 1
            break

print(cnt if cnt else "I must watch Star Wars with my daughter")