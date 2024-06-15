'''
3 2 1 2
[ans] 3
'''
'''
3 2 0 2
[ans] 2
'''
'''
11 2 1 0 50 100 70 100 50 0 2 1
[ans] 250
'''
'''
6 1 2 4 3 5 6
[ans] 12

17 30 6 18 25 8 27 19 29 7 28 6 11 15 30 1 10 3
[ans] 84
'''
# https://www.acmicpc.net/board/view/73359

def solve():

    ns = list(map(int, input().split()))
    while ns[0] != 0:
        ans = 0

        n, ns = ns[0], ns[1:]
        # for new_ns in [[0]+ns[:]]:
        for new_ns in [[0]+ns[:], [0]+ns[:][::-1]]:
            s = [[0, 0]]
            for i in range(1, n+1):
                if new_ns[i] == 0:
                    while s[-1][1] > 0:
                        h = s.pop()[1]
                        ans = max(ans, h*((i-1)-s[-1][0]))
                    s = [[i, 0]]
                else:
                    while s and s[-1][1] >= new_ns[i]:
                        s.pop()
                    s.append([i, new_ns[i]])
                    ans = max(ans, s[-1][1]*(s[-1][0]-s[-2][0]))

            while s[-1][1] > 0:
                h = s.pop()[1]
                ans = max(ans, h*(n-s[-1][0]))

        print(ans)
        ns = list(map(int, input().split()))

solve()