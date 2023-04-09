# 2023 가지컵

# A번 - 가지 교배
# def solve():
#     n = int(input())
#     species = list(input().split())

#     m, _ = map(int, input().split())
#     pos = False
#     for _ in range(m):
#         idxs = list(map(int, input().split()))
#         p_check = False
#         for i in idxs:
#             if species[i-1] == 'P':
#                 p_check = True
#                 break

#         if not p_check:
#             pos = True
#             break

#     print("W") if pos else print("P")

# solve()


# B번 - 가지 산사태
# 어떻게 효율적으로 풀 수 있을까 ~
# import sys
# input = sys.stdin.readline

# def solve():
#     N, M, K = map(int, input().split())
#     hs = [K]*N
#     ans = -1
#     for cmd_num in range(M):
#         flooded = False
#         ti, ri = list(map(int, input().split()))
#         for i in range(ti):
#             hs[i] -= ri
#             if hs[i] < 0:
#                 print(cmd_num+1, i+1)
#                 return

#     print(ans)

# solve()


# 밥 먹으면서 생각해보니까 모든 인덱스를 처리할 필요가 없다
# import sys
# input = sys.stdin.readline

# def solve():
#     _, M, K = map(int, input().split())
#     h = K
#     for cmd_num in range(M):
#         _, ri = list(map(int, input().split()))
#         h -= ri
#         if h < 0:
#             print(cmd_num+1, 1)
#             return

#     print(-1)

# solve()