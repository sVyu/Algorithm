import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())

    if 3*a > b:
        print(3*a-b)
    elif 3*a <= b <= 4*a:
        print(0)
    else: # 4*a < b:
        gap = (b//4)+(1 if b%4 else 0)-a

        ans = gap
        new_a = a+gap
        if 3*new_a > b:
            ans += 3*new_a-b
        # else if 3*new_a <= b <= 4*new_a:

        print(ans)