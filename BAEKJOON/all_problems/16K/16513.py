def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def solve():
    n, repeat = input().split()

    ns = n.split('.')
    len_after_decial_point = len(ns[1])
    # print(len_after_decial_point)

    n = int(''.join(ns))
    repeat = int(repeat)

    a = n-n//(10**repeat)
    b = (10**(repeat)-1)*(10**(len_after_decial_point-repeat))

    gcd_ab = gcd(a,b)
    print(f'{a//gcd_ab}/{b//gcd_ab}')

solve()