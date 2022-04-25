# 10869 사칙연산

# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(int(a/b)) # 아니 ㅋㅋㅋ
# print(a%b)


# 10430 나머지
# A, B, C = map(int, input().split())
# print((A+B)%C)
# print(((A%C)+(B%C))%C)
# print((A*B)%C)
# print((A%C)*(B%C)%C)

# 2558 A + B -2
# a = int(input())
# b = int(input())
# print(a+b)
# a, b = map(int, input().split())
# print(a+b)

# 2588 곱셈
"""
a = int(input())
b = int(input())
b_temp = b
c = []
while b_temp > 1:
    # print(b_temp)
    c.append(int(b_temp%10))
    b_temp /= 10

# print(c)
# c.reverse()
# print(c)

while len(c):
    # print(c[0])
    print(a*c[0])
    del c[0]

print(a*b)
# 머리 속에 로직은 그려지는데 코드 문법이..
# for문으로 뒤에서부터 10 → 100 으로 나누어서 각 자리수의 숫자로 분리
# 이를 순서대로 하나씩 출력, 최종적으로는 단순 곱셈값 혹은 더한값 출력
# I did it !
"""

# 3046 R2

# S = (R1 + R2)/2
# R2 = 2S -R1

# a, b = map(int, input().split())
# print(2*b - a)

# 2163 초콜릿 자르기
# logical thinking problem
# a, b = map(int, input().split())
# if a > b:
#     a, b = b, a
# print((b-1)+((a-1)*b))

# 11021 A+B-7
# 11022 A+B - 8

# row_num = int(input())
# num_list = []
# check = 0

# while check < row_num:
#     num_list.append([])
#     a, b = map(int, input().split())
#     num_list[check].extend([a, b])
#     check += 1

# # print(num_list)

# check = 0
# while check < row_num:
#     # print("Case #{0}: {1}" .format(check+1, num_list[check][0] + num_list[check][1]))
#     print("Case #{0}: {1} + {2} = {3}" .format(check+1, num_list[check][0], \
#             num_list[check][1], num_list[check][0]+num_list[check][1]))
#     check += 1


# 10699 오늘 날짜

# YYYY-MM-DD
# 채점 서버는 시간대 UTC+0, 즉 9시간을 빼야 함
# import datetime
# from datetime import date

# # 2022-04-25
# # today = date.today()
# # print(today)
# # 이게 정답..? 9시간 연산을 안 넣었는데..
# # 안 넣는 게 맞는 답

# # 2022-04-25 16:13:07.465844
# # d = datetime.datetime.now()
# # print(d)

# # 07:00:00
# # test1 = datetime.time(7)
# # print(test1)

# # 시간 연산 → timedelta
# """
# # d = date.today()
# # print(d)

# # td = datetime.timedelta(hours=23)
# # print(d + td)
# """

# now = datetime.datetime.now()
# td = datetime.timedelta(hours=10)

# ans = now + td
# # print(now+td)
# print(ans)


# 7287 등록 - 크롤링
# print("14")
# print("vyu")

# 2525 오븐 시계
# a, b = map(int, input().split())
# gap = int(input())

# b += gap
# while b >= 60:
#     b -= 60
#     a += 1

# if a >= 24:
#     a -= 24

# print(a, b)


# 2530 인공지능 시계

# a, b, c = map(int, input().split())
# gap = int(input())

# c += gap
# if c >= 60:
#     # b += int(c/60)
#     b += c//60
#     c %= 60

# if b >= 60:
#     a += b//60
#     b %= 60

# if a >= 24:
#     a %= 24
#     # a -= 24

# print(a, b, c)


# 2914 저작권
# a, b = map(int, input().split())
# print(a*(b-1)+1)


# 5355 화성 수학
# 조금 더 효율적인 코드 작성이 가능하지 않을까..

# num = int(input())
# exp_list = []
# row_check = 0

# while row_check < num:
#     exp_list.append(input().split())

#     # exp_list.append([])
#     # exp_list[row_check].extend(input().split())
#     # 이 쉬운 걸 놓쳤네

#     row_check += 1
#     # char = num(input())
#     # exp_list[row_check].append(char)
    
# # print(exp_list)

# row_check = 0
# ans = 0

# while row_check < num:
#     col_check = 1
#     ans = float(exp_list[row_check][0])
#     # print(ans)
#     # print("len : {0}", len(exp_list[row_check]))

#     while col_check < len(exp_list[row_check]):
#         if exp_list[row_check][col_check] == '@':
#             ans *= 3
#         elif exp_list[row_check][col_check] == '%':
#             ans += 5
#         elif exp_list[row_check][col_check] == '#':
#             ans -= 7
#         else:
#             print("error\n")
        
#         col_check += 1

#     print("{0:.2f}".format(ans))
#     row_check += 1


# 2675 문자열 반복


# a = [input().split()]
# print(a)

line_num = int(input())

s_list = [input().split() for _ in range(line_num)]
# print(s_list)

for num in range(len(s_list)):
    out_array = list(s_list[num][1])
    # print(out_array)
    # print("haha")

    for num2 in range(len(out_array)):
        # for k in s_list[num][0]:
        for k in range(int(s_list[num][0])):
            # print("{0}, {1}" .format(num2, k))
            print(out_array[num2], end='')

    print()