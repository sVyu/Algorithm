mod = int(1e9)+7

# divide_and_conquer, a^n
def dac(a, n):
    if n <= 1:
        return a
    elif n % 2:
        return (a*dac(a, n-1)) % mod
    else:
        half_square_n = dac(a, n//2)
        return (half_square_n*half_square_n) % mod

def solve():
    for _ in range(int(input())):
        N = int(input())

        if N <= 2:
            print(1)
            continue
        else:
            print(dac(2, N-2))

solve()