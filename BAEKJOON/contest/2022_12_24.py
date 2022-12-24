# 2022 제1회 미적확통컵

# A번 - 연속인가? ?
# k = int(input())
# a, b, c, d = map(int, input().split())

# if a*k + b == c*k + d:
#     print("Yes", a*k + b)
# else:
#     print("No")


# B번 - 수열의 극한값
# b, c, a1, a2 = map(int, input().split())
# n = [0]*1001
# n[0], n[1] = a1, a2
# for idx in range(2, 1001):
#     n[idx] = b*n[idx-1] + c*n[idx-2]

# print(n[-1]/n[-2])