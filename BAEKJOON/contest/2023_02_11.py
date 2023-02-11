# A번 - 소수가 아닌 수

# def check_prime(n):
#     if n == 1: return False
#     elif n == 2 : return True
#     elif n % 2 == 0 : return False
#     else:
#         for div_num in range(3, n//3+1, 2):
#             if n % div_num == 0:
#                 return False
#         return True

# def solve():
#     N = int(input())
#     while check_prime(N+1):
#         N += 1

#     print(N+1)

# solve()


# 수정
# def solve():
#     N = int(input())
#     if N < 10:
#         print(N+11 if N % 2 == 1 else N+12)
#     else:
#         print(N+1 if N % 2 == 1 else N)

# solve()