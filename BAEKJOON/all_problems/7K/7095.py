N = int(input())
mod = int(1e9)
now, len_now = 1, 1
ans = []

for k in range(1, int(1e5)):
    now *= k

    str_now = str(now)
    if len(str_now) <= 8:
        len_now = len(str_now)
    else:
        len_now += len(str_now[8:])

    now = int(str_now[:8])

    # ans
    if len_now > N:
        break
    else:
        if len_now == N:
            ans.append(k)

if ans:
    print(len(ans))
    print(*ans)
else:
    print("NO")

'''
10 ~ 99 -> 1 �ڸ��� 90 �ڸ� ����
100     -> 2 �ڸ��� 1800
1000    -> 3 �ڸ��� 27000
10000   -> 4 �ڸ��� 360000

N�� �ִ� 15�� -> 36352! ���� ����
'''

# import math

# def prime_check(n):
#     if n == 1: return False
#     elif n == 2: return True
#     elif n%2 == 0: return False
#     else:
#         for k in range(3, math.isqrt(n)+1, 2):
#             if n%k == 0:
#                 return False
#         return True