import sys
input = sys.stdin.readline
import math

valid_d_square = 256 # (6+10)**2
for _ in range(int(input())):
    T, X = input().split()
    T = int(''.join(T.split('.')))
    X = int(X)
    # print(T, X)

    a = math.tan(math.pi*X/180)
    h = a*T
    wall_hit_cnt = int(h*10+425)//850

    c = -a*T + wall_hit_cnt*85
    d_square = (c**2)/((a**2)+1)
    print("yes" if d_square <= valid_d_square else "no")
#     print("yes" if (c**2) <= valid_d_square*((a**2)+1) else "no")