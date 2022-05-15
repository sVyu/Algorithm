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

# # a = [input().split()]
# # print(a)

# line_num = int(input())

# s_list = [input().split() for _ in range(line_num)]
# # print(s_list)

# for num in range(len(s_list)):
#     out_array = list(s_list[num][1])
#     # print(out_array)
#     # print("haha")

#     for num2 in range(len(out_array)):
#         # for k in s_list[num][0]:
#         for k in range(int(s_list[num][0])):
#             # print("{0}, {1}" .format(num2, k))
#             print(out_array[num2], end='')

#     print()

############################# 2022/04/26
# 2935 소음
# list_a = [input() for _ in range(3)]
# # print(list_a) # 이 부분 주석처리 하는 것 까먹음

# if list_a[1] == '+':
#     print(int(list_a[0])+int(list_a[2]))
# elif list_a[1] == '*':
#     print(int(list_a[0])*int(list_a[2]))
# else:
#     print("not supported operator")

# 9498 시험 성적
# test_score = int(input())

# if test_score >= 90:
#     print("A")
# elif test_score >= 80:
#     print("B")
# elif test_score >= 70:
#     print("C")
# elif test_score >= 60:
#     print("D")
# else:
#     print("F")

# 10817 세 수
# num_list = list(map(int, input().split()))
# # print(num_list)
# num_list.sort()
# # print(num_list)
# print(num_list[-2])

# 11653 소인수분해
# num = int(input())

# if num == 1:
#     exit()

# div = 2 # 나누는 수, divisor
# num_list = []

# while num > 1:
#     if num % div == 0:
#         num_list.append(div)
#         num /= div
#         continue

#     elif num < div:
#         break

#     else:
#         div += 1

# # print([num_list[i] for i in range(len(num_list))])
# for i in range(len(num_list)):
#     print(num_list[i])

# 1789 수들의 합
# num = int(input())

# sum = 0
# ans = 0

# while num >= sum:   # 등호가 있어야 함
#     ans += 1
#     sum += ans

# ans -= 1
# print(ans)

# 2753 윤년
# year = int(input())
# # if year % 4 == 0 & (((year % 100) != 0) | ((year % 400) == 0)):
# if (year % 4 == 0) & ((year % 100 != 0) | ((year % 400) == 0)):
#     print(1)

# else: print(0)

# 10039 평균 점수
# num_list = [int(input()) for _ in range(5)]
# for x in range(5):
#     if(num_list[x] < 40):
#         num_list[x] = 40

# print(int(sum(num_list)/5))


# 1934 최소공배수
# num = int(input())
# num_list = [input().split() for _ in range(num)]

# # print(num_list)
# # 유클리드 호제법
# def gcd (a, b):
#     while b > 0:
#         a, b = b, a%b
#     return a

# def lcm (a,b):
#     return int(a * b / gcd(a,b))

# for x in range(num):
#     print(lcm(int(num_list[x][0]), int(num_list[x][1])))


# 2480 주사위 세 개

# num_list = list(map(int, input().split()))
# num_list.sort()

# if (num_list[0] == num_list[1]) & (num_list[1] == num_list[2]):
#     print(10000 + num_list[0]*1000)
# elif (num_list[0] == num_list[1]) | (num_list[1] == num_list[2]):
#     print(1000 + num_list[1]*100)
# else:
#     print(num_list[2]*100)


# 4101 크냐?
# num_list = []
# count = 0

# while True:
#     num_list.append(list(map(int, input().split())))
#     if (num_list[count][0] == 0) & (num_list[count][1] == 0):
#         del num_list[count]
#         break
#     count += 1

# # print(num_list)
# for i in range(len(num_list)):
#     if(num_list[i][0] > num_list[i][1]):
#         print("Yes")
#     else:
#         print("No")


# 10156 과자
# num_list = list(map(int, input().split()))
# needed_money = num_list[0] * num_list[1] - num_list[2]

# if(needed_money < 0):
#     print(0)
# else:
#     print(needed_money)


# 3009 네 번째 점
# num_list = [list(map(int, input().split())) for _ in range(3)]
# # print(num_list)
# ans_list =[]

# for i in range(2):
#     if num_list[0][i] == num_list[1][i]:
#         ans_list.append(num_list[2][i])

#     elif num_list[0][i] == num_list[2][i]:
#         ans_list.append(num_list[1][i])
    
#     else:
#         ans_list.append(num_list[0][i])

# print(ans_list[0], ans_list[1])


# 2476 주사위 게임
# num = int(input())
# num_list = [list(map(int, input().split())) for _ in range(num)]
# # print(num_list)
# reward_list = []

# for i in range(num):
#     num_list[i].sort()
#     if (num_list[i][0] == num_list[i][1]) & (num_list[i][1] == num_list[i][2]):
#         reward_list.append(10000 + num_list[i][0] * 1000)
#     elif (num_list[i][0] == num_list[i][1]) | (num_list[i][1] == num_list[i][2]):
#         reward_list.append(1000 + num_list[i][1] * 100)
#     else:
#         reward_list.append(num_list[i][2]*100)

# # print(reward_list)
# reward_list.sort()
# print(reward_list[-1])


# 2754 학점계산
# grade_dict = {  "A+":"4.3", "A0": "4.0", "A-": "3.7",\
#                 "B+":"3.3", "B0": "3.0", "B-": "2.7",\
#                 "C+":"2.3", "C0": "2.0", "C-": "1.7",\
#                 "D+":"1.3", "D0": "1.0", "D-": "0.7",\
#                 "F" :"0.0"}

# # print(type(grade_dict))
# # print(grade_dict)

# grade = input()
# print(grade_dict[grade])


# 2884 알람 시계
# h, m = map(int, input().split())
# # print(h, m)

# if m >= 45:
#     m -= 45
# else:
#     if(h == 0):
#         h = 24
    
#     h -= 1
#     m += 15

# print(h, m)


# 7567 그릇
# # dishes = [input()]
# dishes = input()
# dishes_list = []
# # 그릇을 하나씩 분리해서 list로
# for i in range(len(dishes)):
#     dishes_list.append(dishes[i])
# # print(dishes_list)

# height = 10

# for i in range(len(dishes_list)-1):
#     print(i)
#     if(dishes_list[i+1] == dishes_list[i]):
#         height += 5
#     else:
#         height += 10

# print(height)


# 5063 TGN
# num = int(input())
# num_list = [list(map(int, input().split())) for _ in range(num)]
# # print(num_list)
# ad_str_list = []

# for i in range(len(num_list)):
#     benefit = (num_list[i][1] - num_list[i][0] - num_list[i][2])
#     if benefit > 0:
#         print("advertise")
#     elif benefit == 0:
#         print("does not matter")
#     else:
#         print("do not advertise")

# 10102 개표
# num = int(input())
# vote = list(input())

# # print(vote)
# if vote.count('A') > (num/2):
#     print("A")
# elif vote.count('B') > (num/2):
#     print("B")
# else:
#     print("Tie")


# 10886     0 = not cute/ 1 = cute
# num = int(input())
# num_list = [int(input()) for _ in range(num)]

# check = 0
# for i in range(len(num_list)):
#     if(num_list[i] == 1):
#         check += 1

# # 조건) num 은 홀수
# if check > (num/2):
#     print("Junhee is cute!")
# else:
#     print("Junhee is not cute!")


# 10988 팰린드롬인지 확인하기
# word_list = list(input())
# # print(word_list)

# check = 1
# for i in range(int(len(word_list)/2)):
#     if(word_list[i] != word_list[-(i+1)]):
#         check = 0
#         break
#     else:
#         continue

# print(check)


# 5086 배수와 약수
# result_list = []
# while True:
#     data_list = list(map(int, input().split()))
    
#     if (data_list[0] == 0) & (data_list[1] == 0):
#         break
#     elif(data_list[1] % data_list[0] == 0):
#         result_list.append("factor")
#     elif(data_list[0] % data_list[1] == 0):
#         result_list.append("multiple")
#     else:
#         result_list.append("neither")

# for i in range(len(result_list)):
#     print(result_list[i])


# 5717 상근이의 친구들
# result_list = []
# while True:
#     data_list = list(map(int, input().split()))
#     if (data_list[0] == 0) & (data_list[1] == 0):
#         break
#     else:
#         result_list.append(data_list[0]+data_list[1])

# for i in range(len(result_list)):
#     print(result_list[i])


# 9610 사분면
# num = int(input())
# point_list = [list(map(int,input().split())) for _ in range(num)]
# # print(point_list)
# # result_list = [0]*5     # index : Q1, Q2, Q3, Q4, AXIS
# result_list = [0 for _ in range(5)]
# # print(result_list)

# for i in range(num):
#     if(point_list[i][1] > 0):
#         if(point_list[i][0] > 0):
#             result_list[0] += 1     # 1사분면
#         elif(point_list[i][0] < 0):
#             result_list[1] += 1     # 2사분면
#         else:
#             result_list[4] += 1     # AXIS

#     elif(point_list[i][1] < 0):
#         if(point_list[i][0] < 0):
#             result_list[2] +=1      # 3사분면
#         elif(point_list[i][0] > 0):
#             result_list[3] += 1     # 4사분면
#         else:
#             result_list[4] += 1     # AXIS

#     else:
#         result_list[4] += 1         # AXIS

# for i in range(num):  이 부분 실수
# for i in range(5):
#     if(i == 4):
#         print("AXIS: {0}".format(result_list[i]))
#     else:
#         print("Q{0}: {1}".format((i+1), result_list[i]))


# 8958 OX퀴즈
# num = int(input())
# score_list = []
# for i in range(num):
#     o_score = 0
#     ones_score_sum = 0
#     ans_list = list(str(input()))
#     for j in range(len(ans_list)):
#         if(ans_list[j] == 'O'):
#             o_score += 1
#             ones_score_sum += o_score
#         else:           # 'X'
#             o_score = 0
#     score_list.append(ones_score_sum)

# for i in range(num):
#     print(score_list[i])


# 9506 약수들의 합
# num_list = []
# while True:
#     num = int(input())
#     if(num == -1):
#         break
#     num_list.append(num)
# # print(num_list)

# def check_perfect_number(num):
#     div_list = [1]
#     div = 1
#     while True:
#         div += 1
#         if (num % div == 0) & (num != div):
#             div_list.append(div)
#             # print("test2, {0}, {1}" .format(num, div))
#         elif num <= div :
#             break
#         else:
#             continue
    
#     if(num == sum(div_list)):
#         print("{0} = ".format(num), end='')
#         for i in range(len(div_list)-1):
#             print("{0} + ".format(div_list[i]), end='')
#         print(div_list[-1])
#     else:
#         print("{0} is NOT perfect.".format(num))
#     # print("{0}의 약수 : {1}, sum:{2}".format(num, div_list, sum(div_list)))

# for i in range(len(num_list)):
#     check_perfect_number(num_list[i])


# 10162 전자레인지
# cooking_time = int(input())
# hms_list = [0]*3

# if cooking_time % 10 != 0:
#     print(-1)
#     exit()
# else:
#     if(cooking_time >= 300):
#         hms_list[0] = cooking_time // 300
#         cooking_time %= 300
    
#     if(cooking_time >= 60):
#         hms_list[1] = cooking_time // 60
#         cooking_time %= 60
    
#     hms_list[2] = cooking_time // 10

# print("{0} {1} {2}".format(hms_list[0], hms_list[1], hms_list[2]))


# 10103 주사위 게임
# num = int(input())
# dice_list = [list(map(int, input().split())) for _ in range(num)]
# score_list = [100] * 2

# for i in range(num):
#     gab = dice_list[i][0] - dice_list[i][1]
#     if gab > 0:
#         score_list[1] -= dice_list[i][0]

#     elif gab < 0:
#         score_list[0] -= dice_list[i][1]

#     else:
#         continue

# print(str(score_list[0])+'\n'+str(score_list[1]))


# 10214 Baseball
# import os

# num = int(input())
# sum_list = [0] * 2
# check = 0
# while check < (num*9):
#     score_list = list(map(int, input().split()))
#     for i in range(2):
#         sum_list[i] += score_list[i]

#     if( (check+1) % 9 == 0):
#         if(sum_list[0] > sum_list[1]):
#             print("Yonsei")
#         elif(sum_list[0] < sum_list[1]):
#             print("Korea")
#         else:
#             print("Draw")
#             # os.system("pause")

#         sum_list = [0] * 2
#     check += 1

# 11557 Yangjojang of The Year

# num_of_test_case = int(input())
# winner_list = []

# for i in range(num_of_test_case):
#     num_of_col = int(input())
#     col_list = [input().split() for _ in range(num_of_col)]

#     winner = col_list[0][0]
#     for j in range(len(col_list)-1):
#         if(int(col_list[j][1]) < int(col_list[j+1][1])):
#             winner = col_list[j+1][0]

#     # print(winner)
#     winner_list.append(winner)

# for i in range(len(winner_list)):
#     print(winner_list[i])


# 10757 큰 수 A+B
# a, b = map(int, input().split())
# print(a+b)


# 2562 최댓값
# num_list = [int(input()) for _ in range(9)]

# max_value = max(num_list)
# for i in range(len(num_list)):
#     if(max_value == num_list[i]):
#         print(max_value)
#         print(i+1)


# 13333 Q-인덱스
# num = int(input())
# num_list = list(map(int, input().split()))
# num_list.sort()

# index = 0
# # k 번 이상 인용된 논문 k편 이상, k는 0부터 num까지
# for k in range(num, -1, -1):
#     count1 = 0
#     count2 = 0

#     for i in range(num-1, -1, -1):
#         if(num_list[i] >= k):
#             count1 += 1
#             index = i
#         else: break

#     for j in range(index):
#         if(num_list[i] <= k):
#             count2 += 1
#         else: break

#     if( (k <= count1) & ( k >= count2) ):
#         # print(k, count1, count2)
#         print(k)
#         break


# 1929 소수 구하기
# 시간 초과
# import math

# m, n = map(int, input().split())

# def prime_check(num):
#     if num == 1: return False

#     for i in range(2, int(math.sqrt(num))+1):
#         if num % i == 0 : return False
    
#     return True

# for i in range(m, n+1):
#     if prime_check(i):
#         print(i)

# for i in range(m, n+1):
#     prime_number_check = 1
#     for j in range(2, int(math.sqrt(i))+1):
#         if(i % j == 0):
#             prime_number_check = 0
#             break

#     if(prime_number_check == 1):
#         print(i)


# 4344 평균은 넘겠지

# c = int(input())
# score = []         # score 리스트 안에 또 각각의 리스트를 만들 것이다.
# sum_score = []     # score 리스트 안에 있는 각 리스트의 점수들의 합을 모아둘 것이다.
# average = []       # score 리스트 안에 있는 각 리스트의 평균들을 모아둘 것이다.
# count = [0] * c    # 한 리스트에서 평균 넘는 애들 숫자 세기

# for i in range(c):                                        # 각 리스트의 점수 입력 및 평균까지 구하기
#     score.append(list(map(int, input().split())))         # 한 리스트의 점수들을 입력해서 score 리스트에 추가하기
#     sum_score.append(sum(score[i][1:(score[i][0]+1)]))    # 그 리스트 안에 있는 점수들 합해서 sum_score 리스트 안에 추가하기
#     average.append(sum_score[i] / score[i][0])            # 그 sum_score에 합한 값을 점수 개수로 나누어서 average 리스트에 추가하기

# # 평균 넘는 애들을 카운트해서 비율 구하기
#     for k in range(1, score[i][0] + 1):
#         if score[i][k] > average[i]:
#             count[i] += 1
#     # print(f'{round(count[i] / score[i][0] * 100, 3)}%')
#     print('{0:.3f}%'.format(round(count[i] / score[i][0] * 100, 3)))

# num = int(input())
# num_list = [list(map(int, input().split())) for _ in range(num)]
# # print(num_list)

# # 0행부터 num-1 행까지
# for i in range(num):
#     avg = sum(num_list[i][1:])/num_list[i][0]   # 각 행마다 평균(avg) 계산
#     # print(avg)

#     count = 0
#     for j in range(1, num_list[i][0]+1):
#         if(num_list[i][j] > avg): count += 1    # 평균보다 크면 count+1
    
#     print('{0:.3f}%'.format(round((count/num_list[i][0]) * 100, 3)))    # 형식에 맞게 출력

# 10757
# p, q = input().split()

# d= max(len(p), len(q))
# p = p.zfill(d+1)
# q = q.zfill(d+1)
# r = ''
# # print(d, p, q)

# c = 0
# # 1 부터 d+1 까지
# for i in range(1, d+2):
#     t = int(p[-i]) + int(q[-i])
#     r = str(t % 10 + c) + r
#     c = t // 10 # 다음 자리 수 +c 만큼
#     # print(t, r, c)

#     # t = int(p[-i]) + int(q[-i]) + c
#     # r = str(t % 10) + r
#     # c = t // 10
#     # print(t, r, c)

# print(r.lstrip('0'))


# for class ~
# 1152 단어의 개수
# print(len(list(map(str, input().split()))))

# 1157 단어 공부
# print(ord('A'))
# print(chr(65))

# str_input = list(input())
# # print(str_input)
# # 각 알파벳을 카운트 할 list
# count_list = [0] * 26

# for i in range(len(str_input)):
#     # 대문자 A(65) ~ Z
#     if(65 <= ord(str_input[i]) <= 90):
#         count_list[ord(str_input[i])-65] += 1
#     # 소문자 a(97) ~ z
#     else:
#         count_list[ord(str_input[i])-97] += 1
# # print(count_list)

# # count_list의 최대값을 이용해서 그 최대값이 몇 개(max_value_count) 있고 index는 몇인지
# max_value = max(count_list)
# max_value_count, max_value_index = 0, 0
# # print(count_list.index(max_value))
# for i in range(26):
#     if(count_list[i] == max_value):
#         max_value_count += 1
#         max_value_index = i
# # print(max_value_count)

# if(max_value_count == 1): print(chr(65 + max_value_index))
# else: print("?") # 2개 이상


# 1546 평균
# num = int(input())
# num_list = list(map(int, input().split()))
# # print(num_list)

# # 새로운 점수 : num_list[index] / max(num_list) * 100 이므로 아래는 평균
# print(sum(num_list)/(max(num_list)*num) * 100)


# 11720 숫자의 합
# list_len = int(input())
# int_list = list(map(str, input()))

# sum = 0
# for i in range(list_len):
#     sum += int(int_list[i])

# print(sum)


# 1110 더하기 사이클
# num = int(input())

# # 10의 자리, 1의 자리
# tens_place, ones_place = num // 10, num % 10
# # print(tens_place, ones_place)

# # 새로 만든 숫자 : -1로 초기화
# new_number = -1 # new_number = 0
# count = 0
# while num != new_number:
#     new_number = (ones_place * 10) + (tens_place + ones_place) % 10
#     count += 1
#     tens_place, ones_place = new_number // 10, new_number % 10
#     # print(new_number, count)

# print(count)


# 4690 완전 세제곱
# a;b;c;d;i;j;k;l;main()
# for(i=2;100>i;i++){
#     for(j=2;100>j;j++){
#         for(k=j;100>k;k++){
#             for(l=k;100>l;l++){
#                 if(i*i*i==j*j*j+k*k*k+l*l*l){
#                     printf("Cube = %d, Triple = (%d,%d,%d)\n",i,j,k,l);
#                 }
#             }
#         }
#     }
# }

# for i in range(2, 101):
#     for j in range(2, i):
#         for k in range(j, i):
#             for m in range(k, i):
#                 # if(i**3 == ((j**3) + (k**3) + (m**3))):
#                 if((i*i*i) == ((j*j*j) + (k*k*k) + (m*m*m))):
#                     print("Cube = {0}, Triple = ({1},{2},{3})".format(i, j, k, m))


# 2805 나무 자르기
# 시간 초과
# import sys

# n, m = map(int, sys.stdin.readline().rstrip().split())
# tree_height_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse = True)
# print(tree_height_list)

# # 제일 높은 나무의 높이를 기점으로 cutting_height 변수 초기화
# # cutting_height = max(tree_height_list)

# cutting_height = int((tree_height_list[0] + tree_height_list[n-1])/2)
# # print(cutting_height)

# # 이분 탐색
# while True:
#     for i in range(n):
#         if((tree_height_list[i] - cutting_height) > 0):
#             sum += tree_height_list[i] - cutting_height
#         else: break
    
#     if(sum >= m): cutting_height = int((cutting_height + tree_height_list[0])/2)
#     else: cutting_height = int((cutting_height + tree_height_list[0])/2)


# brute force
# # 1씩 줄이면서 계산
# for i in range(cutting_height, -1, -1):
#     sum = 0
#     # 큰 나무부터 cutting을 해서 남는 값이 있으면 sum에 합산
#     for j in range(n-1, -1, -1):
#         if((tree_height_list[j] - i) > 0):
#             sum += tree_height_list[j] - i
#             # print(i, j, sum)
#         # 0이하의 값 → cutting 기준 이하의 나무 길이 → 정렬돼있으므로 확인 할 필요 없음
#         else:
#             break

#     # sum의 값이 m 이상이 되면 조건 충족이므로 break
#     if(sum >= m):
#         cutting_height = i
#         break

# print(cutting_height)


# 2869 달팽이는 올라가고 싶다
# import math
# a, b, v = map(int, input().split())

# # print(math.ceil(v/(a - b)))
# days = math.ceil(v/(a - b))
# minus_days = 0
# min_days = 0

# while True:
#     minus_days += 1
#     if()


# 두 수 비교하기 1330
a, b = map(int, input().split())
if(a > b): print(">")
elif(a < b): print("<")
else: print("==")