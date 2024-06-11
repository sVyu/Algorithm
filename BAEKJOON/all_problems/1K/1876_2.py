# import sys
# input = sys.stdin.readline
# import math

# for _ in range(int(input())):
#     T, X = input().split()
#     T = int(''.join(T.split('.')))
#     X = int(X)

#     moved_d = 85/math.tan(math.pi*X/180)
#     # print(moved_d)
#     # print(math.pi)

#     quo = int(T//moved_d)
#     vx = T-quo*moved_d
#     hit = False

#     while vx >= -16:
#         if (-16) <= vx <= 16:
#             hit = True
#             break
#         vx -= moved_d

#     print("yes" if hit else "no")