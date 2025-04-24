# ref : https://jeongboclass.tistory.com/160

def solve():
    n = int(input())
    zs = list(map(int, input().split()))

    ans = n
    for i in range(n-1):
        for j in range(i+1, n):
            gap = zs[j]-zs[i]
            if(gap % (j-i)): continue

            d = gap // (j-i)
            target = zs[i]-(i*d)
            cnt = 0
            for k in range(n):
                if(target != zs[k]):
                    cnt += 1
                target += d

            ans = min(ans, cnt)

    print(ans)

solve()