def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

n, m, k = map(int, input().split())
n += 1
m += 1

intersec = k//(n*m//gcd(n,m))
print(k-(k//n)-(k//m)+intersec, intersec, (k//m)-intersec, (k//n)-intersec)