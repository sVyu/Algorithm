def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def solve():
    size = 1001
    cnts = [3]*size
    shown = [[False]*size for _ in range(size)]
    shown[1][1] = True
    for x in range(2, size):
        can_see = 0
        for y in range(1, x):
            gcd_xy = gcd(x, y)
            minx, miny = x//gcd_xy, y//gcd_xy
            if not shown[minx][miny]:
                shown[minx][miny] = True
                can_see += 1

        cnts[x] = cnts[x-1] + 2*can_see

    for _ in range(int(input())):
        print(cnts[int(input())])

solve()