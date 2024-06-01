import sys
input = sys.stdin.readline

# def f(n):
#     val = 1
#     for i in range(2, n+1):
#         val *= i
#     return val

# def c(n, k):
#     val = 1
#     for i in range(n, n-k, -1):
#         val *= i
#     return val//f(k)

def solve():
    N, M = map(int, input().split())
    roads = [set() for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        # roads[a] += (1<<b) # c++ overflow hmm..
        roads[a].add(b)

    ans = 0
    for i in range(1, N):
        for j in range(i+1, N+1):
            len_inter_set = len(roads[i]&roads[j])
            ans += (len_inter_set*(len_inter_set-1))//2

    print(ans)

solve()