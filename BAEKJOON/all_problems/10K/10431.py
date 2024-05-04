import sys
input = sys.stdin.readline

for case in range(int(input())):
    ans = 0
    ns = list(map(int, input().split()))[1:]

    now = []
    for i in range(20):
        for j in range(i):
            if now[j] > ns[i]:
                ans += i-j
                break
        now = sorted(now+[ns[i]])

    print(case+1, ans)