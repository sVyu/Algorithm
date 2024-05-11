def f(n):
    val = 1
    for k in range(2, n+1):
        val *= k
    return val

def solve():
    N, K = map(int, input().split())
    mod = int(1e4)+7

    val = 1
    for k in range(N, N-K, -1):
        val *= k

    print((val//f(K))%mod)

solve()
