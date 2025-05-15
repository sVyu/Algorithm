def gcd(a, b):
    while(b):
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b//gcd(a,b)

def solve():
    s = input()
    t = input()
    lcm_len = lcm(len(s), len(t))
    # print(lcm_len)

    mul_s = lcm_len//len(s)
    mul_t = lcm_len//len(t)

    fs = s*mul_s
    ft = t*mul_t

    print(1 if fs == ft else 0)

solve()