# 2023/01/21

# parity (홀짝)
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))

#     ans = 0
#     std = a[0] % 2
#     for num in a[1:]:
#         if num % 2 == std:
#             ans += 1
#         else:
#             std = num % 2
#         # print(ans)

#     print(ans)


# B. Emordnilap
# import sys
# input = sys.stdin.readline

# factorial_table = [1, 1] + [0] * (10**5)
# for idx in range(2, len(factorial_table)):
#     factorial_table[idx] = (factorial_table[idx-1]*idx) % (int(1e9)+7)
# # print(factorial_table[3])
# for _ in range(int(input())):
#     N = int(input())
#     print((N * (N-1) * factorial_table[N]) % (int(1e9)+7))


# C. Quiz Master
