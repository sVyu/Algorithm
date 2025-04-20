import sys
input = sys.stdin.readline

def gcd(a, b):
    while(b):
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b//gcd(a,b)

def solve():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())

        for k in range(2, 100001):
            lcm_bk = lcm(b, k)
            # cv : correction_value
            cv_for_left = lcm_bk//b
            cv_for_right = lcm_bk//k

            if((a*cv_for_left) > cv_for_right):
                a = a*cv_for_left-cv_for_right
                b = lcm_bk

                gcd_ab = gcd(a,b)
                a //= gcd_ab
                b //= gcd_ab

            if(a == 1): break

        print(b)

solve()