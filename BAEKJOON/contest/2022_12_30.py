# Good Bye, BOJ 2022! 예비 소집

# def sieve(N):
#     prime_num = [False, False] + [True]*(N-1)
#     for i in range(2, N):
#         if prime_num[i]:
#             for ii in range(2*i, N+1, i):
#                 prime_num[ii] = False

#     return [idx for idx in range(N+1) if prime_num[idx]]

# def solve():
#     N = int(input())
#     n = sieve(120)
#     # print(n)
#     new_n = sorted([n[i]*n[i+1] for i in range(len(n)-1)])
#     # print(new_n)

#     for target in new_n:
#         if target > N:
#             print(target)
#             break

# solve()