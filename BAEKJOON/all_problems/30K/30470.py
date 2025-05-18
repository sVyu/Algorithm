import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    s = []

    for _ in range(n):
        a, b = map(int, input().split())
        if(a == 1):
            s.append([b, 1])
        else:
            if(not s): continue

            th = s[-1][0]-b
            if(th <= 0): s = []

            tot_cnt = 0
            while(s):
                h, cnt = s[-1]
                if(h >= th):
                    tot_cnt += cnt
                    s.pop()
                else:
                    break

            s.append([th, tot_cnt])

    ans = 0
    for h, cnt in s:
        ans += h*cnt
    print(ans)

solve()