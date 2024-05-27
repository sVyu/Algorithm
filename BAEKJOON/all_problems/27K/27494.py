N = int(input())
ans = 0
for k in range(2023, N+1):
    str_k = str(k)
    
    target = "2023"
    ti = 0
    for i in range(len(str_k)):
        if str_k[i] == target[ti]:
            ti += 1
            if ti == 4:
                ans += 1
                break

print(ans)