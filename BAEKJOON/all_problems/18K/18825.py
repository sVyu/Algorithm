# 맞았습니다!   1193
# 맞힌 사람     1017

import math

def prime_check(n):
    if n == 1:          return False
    elif n == 2:        return True
    elif n % 2 == 0:    return False
    else:
        for k in range(3, math.isqrt(n), 2):
            if n % k == 0:
                return False
        return True

# n = 1193+2
n = 1017+2
p = -1
k = 0       # p 이하의 소수의 개수
for val in range(2, n+1):
    if prime_check(val):
        k += 1
        if n % val == 0:
            p = val
            break
print(p, k)

'''
맞았습니다
n       1193
n+2     1195
p       5
k       3
999+k   1002
'''

'''
맞힌 사람
n       1017
n+2     1019
p       1019
k       186
999+k   1185 
'''