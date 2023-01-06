# A - Greatest Convex
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     print(int(input().rstrip())-1)

# B - Quick Sort 
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     k, n = map(int, input().split())
#     p = list(map(int, input().split()))
#     target = 1

#     for num in p:
#         if num == target:
#             target += 1

#     ans = (k-(target-1)) // n
#     if (k-(target-1)) % n != 0:
#         ans += 1
#     print(ans)


# C. Elemental Decompress
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().rstrip().split()))

#     p = [0]*n
#     q = [0]*n
#     p_set = set(i for i in range(1, n+1))
#     q_set = set(i for i in range(1, n+1))

#     idxs = dict()
#     for idx in range(n):
#         idxs[idx] = a[idx]
#     # print(idxs)

#     idxs = sorted(idxs.items(), key=lambda x:(-x[1], x[0]))
#     # print(idxs)

#     pre_val = -1
#     appeared_twice = False
#     pos = True

#     for idx, val in idxs:
#         if pre_val != val:
#             p[idx] = val
#             p_set.remove(val)
#             appeared_twice = False
#         else:
#             if not appeared_twice:
#                 q[idx] = val
#                 q_set.remove(val)
#                 appeared_twice = True
#             else:
#                 pos = False
#         pre_val = val
#     # print(p, q)

#     p_set = sorted(p_set)
#     q_set = sorted(q_set)
#     # print(p_set, q_set)

#     if pos:
#         for idx, val in idxs:
#             if p[idx] != 0:
#                 q[idx] = q_set.pop()
#                 if p[idx] < q[idx]:
#                     pos = False
#                     break
#             else:
#                 p[idx] = p_set.pop()
#                 if q[idx] < p[idx]:
#                     pos = False
#                     break

#     if pos:
#         print("YES")
#         print(*p)
#         print(*q)
#     else: print("NO")


# D
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n = int(input())
#     p = map(int, input().split())