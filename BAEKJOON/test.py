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
# 시간 초과
# import math
# import sys

# a, b, v = map(int, sys.stdin.readline().split())
# v -= a

# print(math.ceil(v/(a-b)) + 1)

# gab = a - b
# days = math.ceil(v / gab)
# minus_days = 0
# min_days = 0

# while True:
#     minus_days += 1
#     if((gab * (days - minus_days) + a) >= v): continue
#         # print(gab, days, minus_days, a, v)
#     else: break
# min_days = days - minus_days
# print(min_days + 2)


# 두 수 비교하기 1330
# a, b = map(int, input().split())
# if(a > b): print(">")
# elif(a < b): print("<")
# else: print("==")


# 팰린드롬수 1259

# while True:
#     num_input = input()
#     if(num_input == '0'): break
#     else:
#         num_list = list(map(int, num_input))
#         # print(num_list)

#         palindrome_check = True
#         for i in range(len(num_list) // 2):
#             if(num_list[i] == num_list[len(num_list)-1-i]): continue
#             else: palindrome_check = False
        
#         if(palindrome_check): print("yes")
#         else: print("no")


# 1018 체스판 다시 칠하기
# import sys
# m, n = map(int, input().split())
# checkboard_list = [list(sys.stdin.readline().rstrip()) for _ in range(m)]
# # print(checkboard_list)

# # m, n은 각각 8이상이므로 check 필요 X
# # i, j : 시작돌 위치
# # 바꿔야 하는 돌의 최대 개수는 64개이므로 min을 64로 설정
# min_count = 64
# for i in range(m-7):
#     for j in range(n-7):
#         count = 0
#         go_stone = {0:'W', 1:'B'}
#         for x in range(0, 8):
#             for y in range(0, 8):
#                 # 시작 돌이 White
#                 if(checkboard_list[i+x][j+y] == go_stone[(x+y)%2]): count += 0
#                 else: count += 1
#         # print(i, j, count, 'W')
#         if(count < min_count): min_count = count

#         count = 0
#         for x in range(8):
#             for y in range(8):
#                 # 시작 돌이 Black
#                 if(checkboard_list[i+x][j+y] == go_stone[(x+y+1)%2]): count += 0
#                 else: count += 1
#         # print(i, j, count, 'B')
#         if(count < min_count): min_count = count

# print(min_count)

# go_stone = {0:'W', 1:'B'}
# print(go_stone[0])
# print(go_stone[2])
# print(go_stone[1])


# 2747 피보나치 수
# 2748 피보나치 수 2
# 2749 피보나치 수 3
# 10826 피보나치 수 4
# 10870 피보나치 수 5

# 11444 피보나치 수 6
# 행렬을 이용한 계산

# num_input = int(input())
# fibonacci_list = [0, 1]
# for i in range(2, num_input + 1):
#     fibonacci_list.append((fibonacci_list[i-1] + fibonacci_list[i-2]))

# print(fibonacci_list[num_input])


# 9471 피사노 주기
# case_num = int(input())
# case_list = [list(map(int, input().split())) for _ in range(case_num)]
# # print(case_list)

# for k in range(case_num):
#     fibonacci_list = [0, 1]
#     i = 1
#     while True:
#         # i : index (i번째 fibonacci 수)
#         i += 1
#         fibonacci_list.append((fibonacci_list[i-1]+fibonacci_list[i-2]) % case_list[k][1])
#         # print(fibonacci_list)
#         if((fibonacci_list[-1] + fibonacci_list[-2]) == 1):
#             break

#     print(k + 1, i)
#     # print(i, fibonacci_list)


# 2749 피보나치 수 3
# 9471 피사노 주기를 먼저 풀어야 가능
# num = int(input())
# fibonacci_list = [0, 1]

# for i in range(2, 1500001):
#     fibonacci_list.append((fibonacci_list[i-1] + fibonacci_list[i-2]) % 1000000)

# print(fibonacci_list[num % 1500000])


# 11444
# num = int(input())
# fibonacci_list = [0, 1]

# for i in range(2, 1500001):
#     fibonacci_list.append((fibonacci_list[i-1] + fibonacci_list[i-2]) % 1000000)

# print(fibonacci_list[num % 1500000])


# 5522 카드 게임
# print(sum([int(input()) for _ in range(5)]))


# 14754 Pizza Boxes
# import sys

# n, m = map(int, sys.stdin.readline().rstrip().split())
# pizza_boxes = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
# # print(pizza_boxes)
# check_pizza_list = [[0] * m  for _ in range(n)]

# # 각 행의 최대 boxes 좌표 check
# for i in range(0, n):
#     max_index = 0
#     for j in range(1, m):
#         if(pizza_boxes[i][j] > pizza_boxes[i][max_index]): max_index = j
#     check_pizza_list[i][max_index] = 1

# # 각 열의 최대 boxes 좌표 check
# for j in range(0, m):
#     max_index = 0
#     for i in range(1, n):
#         if(pizza_boxes[i][j] > pizza_boxes[max_index][j]): max_index = i
#     check_pizza_list[max_index][j] = 1

# # pizza 합계 계산
# sum = 0
# for i in range(n):
#     for j in range(m):
#         # if ([i, j] not in max_index_list): sum += pizza_boxes[i][j]
#         if(check_pizza_list[i][j] == 0): sum += pizza_boxes[i][j]

# # print(max_index_list)
# print(sum)


# 10718 We love kriii
# print("강한친구 대한육군\n강한친구 대한육군")


# 1181 단어 정렬
# num = int(input())

# word_dict = {}
# for i in range(num):
#     word = input()
#     word_dict[word] = len(word)

# # word_dict = sorted(word_dict.items(), key=lambda x:(x[1], x[0]))
# # print(word_dict)

# # 1. 길이순(x[1]), 2.(같은 길이인 경우)사전순(x[0])
# for i in sorted(word_dict.items(), key=lambda x:(x[1], x[0])):
#     print(i[0])


# 1764 듣보잡
# import sys
# n, m = map(int, input().split())

# # 듣잡 dict
# not_heard_dict = {}
# for i in range(n):
#     name = sys.stdin.readline().rstrip()
#     not_heard_dict[name] = i
# # 정렬
# not_heard_dict = sorted(not_heard_dict.items(), key=lambda x:(x[0]))

# # 보잡 dict
# not_seen_dict = {}
# for i in range(m):
#     name = sys.stdin.readline().rstrip()
#     not_seen_dict[name] = i

# # 듣보잡 list
# not_heard_seen_list = []
# for i in range(min([n, m])):
#     if(not_heard_dict[i][0] in not_seen_dict):
#         not_heard_seen_list.append(not_heard_dict[i][0])

# # 듣보잡의 수와 그 명단을 사전순으로 출력(위에서 이미 정렬을 했으므로 사전순으로 출력됨)
# print(len(not_heard_seen_list))
# for i in range(len(not_heard_seen_list)): print(not_heard_seen_list[i])


# 4949 균형잡힌 세상
# import sys

# while True:
#     str_list = list(sys.stdin.readline().rstrip())
#     # print(str_list)
    
#     if((len(str_list) == 1) & (str_list[0] == '.')):
#         break
    
#     stack_list = []

#     symmetry_check = True
#     for i in range(len(str_list)):
#         if (str_list[i] == '('): stack_list.append('(')
#         elif (str_list[i] == '['): stack_list.append('[')

#         elif (str_list[i] == ')'):
#             if(len(stack_list) == 0):
#                 symmetry_check = False
#                 break
#             elif(stack_list.pop() == '('): continue
#             else:
#                 symmetry_check = False
#                 break
#         elif (str_list[i] == ']'):
#             if(len(stack_list) == 0):
#                 symmetry_check = False
#                 break
#             elif(stack_list.pop() == '['): continue
#             else:
#                 symmetry_check = False
#                 break
#         else: continue
    
#     # if(len(stack_list) == 0): print("yes")
#     # else: print("no")

#     # 출력초과 테스트용 코드
#     # 테스트결과, 한 string에 .이 2개 이상인 경우는 없었음
#     dot_count = 0
#     for i in range(len(str_list)):
#         if(str_list[i] == '.'):
#             dot_count += 1
#     if(dot_count > 1):
#         print("haha")

#     if((len(stack_list) == 0) & (symmetry_check == True)): print("yes")
#     else: print("no")


# 2108 통계학
# import math
# import sys

# num = int(input())
# num_list = [int(sys.stdin.readline().rstrip()) for _ in range(num)]
# num_list.sort()

# # 평균
# print(round(sum(num_list)/len(num_list)))

# # 중앙값
# # 길이가 홀수인 경우
# if((len(num_list) % 2) == 1): print(num_list[len(num_list)//2])
# # 짝수인 경우
# else: print(num_list[len(num_list)//2] + num_list[(len(num_list)//2)-1])

# # 최빈값
# num_count_set = {}
# for i in range(len(num_list)):
#     if(num_list[i] not in num_count_set): num_count_set[num_list[i]] = 1
#     else: num_count_set[num_list[i]] += 1

# # -x[1] : 카운트 수로 정렬, x[0] : 같은 카운트에 대해 기존 숫자 오름차순 정렬
# num_count_set = sorted(num_count_set.items(), key=lambda x:(-x[1], x[0]))
# if(len(num_count_set) == 1): print(num_count_set[0][0])
# elif(num_count_set[0][1] == num_count_set[1][1]): print(num_count_set[1][0])
# else: print(num_count_set[0][0])
# # print(num_count_set)

# # 범위
# print(num_list[-1] - num_list[0])


# 2609 최대공약수와 최소공배수
# n, m = map(int, input().split())

# # 최대공약수 - 유클리드 호제법
# def gcd(a, b):
#     while(b!= 0): a, b = b, a % b
#     return a

# # 최소공배수
# def lcm(a, b):
#     return a * b // gcd(a,b)

# print(gcd(n, m))
# print(lcm(n, m))

# 10944 랜덤 게임~~
# from random import *
# print(randint(1, 10000))


# 빠른 A+B
# import sys

# num = int(sys.stdin.readline().rstrip())
# for _ in range(num):
#     num_list = list(map(int, sys.stdin.readline().rstrip().split()))
#     print(sum(num_list))


# 16120 PPAP
# 시간 초과
# str_list = list(input().rstrip())
# # print(str_list)

# while True:
#     if(len(str_list) < 4):
#         print("NP")
#         break
#     elif(str_list == ['P', 'P', 'A', 'P']):
#         print('PPAP')
#         break
#     # 길이 4이상에 PPAP가 아닌 경우
#     else:
#         new_str_list = []
#         # 7인 경우 3까지 검사 range(4)
#         # for i in range(len(str_list)-3):
#         i = 0
#         while True:
#             # index가 str_list 범위를 벗어나면 break
#             if(i >= len(str_list)): break
#             # print(i)
#             # 남은 str_list 길이가 3이하면 PPAP 검사 할 필요가 없으므로 new_str_list에 .extend()
#             if(len(str_list[i:]) <= 3):
#                 new_str_list.extend(str_list[i:])
#                 break
#             # PPAP 검사
#             elif((str_list[i] == 'P') & (str_list[i+1] == 'P') & (str_list[i+2] == 'A') & (str_list[i+3] == 'P')):
#                 new_str_list.append('P')
#                 i += 4
#             # PPAP가 아닌 경우 단순하게 append 추가
#             else:
#                 new_str_list.append(str_list[i])
#                 i += 1
        
#         # 새로운 str_list랑 기존 str_list랑 같은 경우 → 무한 루프 → NP
#         if(new_str_list == str_list):
#             print("NP")
#             break
#         # 아닌 경우, 다음 step 진행
#         else:
#             # print(new_str_list)
#             str_list = new_str_list


# 15881 Pen Pineapple Apple Pen
# str_len = int(input())
# str_list = list(input())

# p_index = []
# for i in range(str_len):
#     if(str_list[i] == 'p'): p_index.append(i)
# # print(p_index)

# count = 0
# for i in p_index:
#     if((i + 3) >= str_len): break
#     elif(str_list[i:i+4] == ['p','P','A','p']):
#         count += 1
#         str_list[i+3] = 'v' # pPApPAp 일 때 1개만 체크하기 위함
#     else: continue
#     # print(str_list)
# print(count)


# 16692 Greedy Scheduler
# n, c = map(int, input().split())
# cart_list = list(map(int, input().split()))

# cashier_number_list = [0] * c

# # 0 ~ n-1 인덱스 까지는 오는 순서대로 받을 수 있음
# for i in range(n):
#     cashier_number_list[i] = i + 1

# # 그 이후의 인덱스에 대해서는 기존 n 까지의 범위 중 최소 값을 가지는 cashier의 index 값을 이용
# for i in range(n, c):
#     min_seconds_index = 0
#     for j in range(1, n):
#         if(cart_list[min_seconds_index] > cart_list[j]): min_seconds_index = j
#     cart_list[min_seconds_index] += cart_list[i]
#     cashier_number_list[i] = min_seconds_index + 1

# for i in range(c):
#     print(cashier_number_list[i], end= ' ')
# # print(cashier_number_list)


# 18787 Mad Scientist
# num = int(input())
# string_A = list(input())
# string_B = list(input())

# flipinator_3000_on = False
# count = 0
# for i in range(num):
#     if(string_A[i] != string_B[i]):
#         # if(~flipinator_3000_on): # 이건 numpy 식
#         if(not flipinator_3000_on):
#             flipinator_3000_on = True
#             count += 1
#         else: continue
#     else:
#         flipinator_3000_on = False
#         continue
#     # print(i, flipinator_3000_on, count)

# print(count)


# 10859 뒤집어진 소수
# 4퍼 13퍼 16퍼 91퍼 → 틀렸습니다
# 4퍼 5퍼 시간 초과 
# import math
# import sys

# input_value = sys.stdin.readline().rstrip()
# num_list = list(map(int, input_value))
# list_len = len(num_list)
# new_num_list = [0] * list_len

# # # 2의 배수나 5의 배수인지 혹은 3의 배수인지 check
# # def multiple_check(list):
# #     if( ((list[-1]%2) == 0) | (list[-1] == 5) | (sum(list) % 3 == 0)):
# #         print("no")
# #         # quit()
# #         sys.exit(0)

# # 소수 체크 함수
# def prime_num_check(num):
#     if num == 1: return False
#     elif num == 2: return True
#     elif num % 2 == 0: return False # 2가 아닌 2의 배수

#     # 3부터 루트(num)까지 check
#     prime_check = True
#     for i in range(3, int(math.sqrt(num))+1, 2):
#         if(num % i == 0):
#             prime_check = False
#             break

#     return(prime_check)

# # list를 숫자로 만드는 함수
# def list_to_num(list):
#     num = 0
#     multiple_value = 1
#     for i in range(list_len-1, -1, -1):
#         num += list[i] * multiple_value
#         multiple_value *= 10
#     return num

# # multiple_check(num_list)
# # 3, 4, 7은 (뒤집으면, 180도 돌리면) 숫자가 아니다, 확인하면서 숫자 돌림(new_num_list)
# for i in range(list_len):
#     if((num_list[i] == 3) | (num_list[i] == 4) | (num_list[i] == 7)):
#         print("no")
#         # quit()
#         sys.exit(0)
#     elif(num_list[i] == 6): new_num_list[list_len-1-i] = 9
#     elif(num_list[i] == 9): new_num_list[list_len-1-i] = 6
#     else: new_num_list[list_len-1-i] = num_list[i]
# # print(num_list)
# # print(new_num_list)
# # multiple_check(new_num_list)

# new_value = list_to_num(new_num_list)

# # 뒤집어진(new) 숫자와 기존 숫자를 체크해서 둘 다 소수면 yes 아니면 no 
# # print(input_value, new_value)
# if(prime_num_check(new_value) & prime_num_check(int(input_value))): print("yes")
# else: print("no")

# 1712 손익분기점
# a, b, c = map(int, input().split())
# if((c-b) <= 0): print(-1)
# else: print((a//(c-b)) +1)


# 2798 블랙잭
# import sys
# input = sys.stdin.readline

# # n은 제시되는 카드 개수, m은 합
# n, m = map(int, input().split())
# num_list = list(map(int, input().split()))
# # print(n, m, num_list)

# sum = 0
# for i in range(n-2):
#     for j in range(i+1, n-1):
#         for k in range(j+1, n):
#             # print(i, j, k)
#             if(sum < (num_list[i] + num_list[j] + num_list[k]) <= m):
#                 sum = num_list[i] + num_list[j] + num_list[k]
#                 # print("sum : ", sum)
# print(sum)


# 1977 완전제곱수
# import math

# m = int(input())
# n = int(input())

# sum = 0
# for i in range(math.ceil(math.sqrt(m)), math.floor(math.sqrt(n))+1):
#     sum += i ** 2

# if(sum == 0): print(-1)
# else:
#     print(sum)
#     print(math.ceil(math.sqrt(m)) ** 2)


# 1966 프린터 큐
# import sys
# from queue import Queue
# input = sys.stdin.readline

# # 입력 데이터로 for 문, 중요도 높은 문서를 확인하기 위해 sorted list 추가
# case_num = int(input())
# for i in range(case_num):
#     n, m = map(int, input().split())
#     test_case = list(map(int, input().split()))
#     test_case_sorted= sorted(test_case.copy())
#     # print(test_case_sorted)

#     # test_case 값에 index를 추가로 포함하는 리스트를 que에 put()
#     que = Queue()
#     count = 0
#     for j in range(n):
#         que.put([test_case[j], j])
#     # print(que.queue)

#     # que가 비어있지 않는 한 get()을 반복하면서 확인
#     while que.qsize():
#         get_value = que.get()
#         # print(get_value)
#         # 우선도가 가장 높은 수일 경우, sorted[-1] pop(), count 증가
#         if(get_value[0] == test_case_sorted[-1]):
#             test_case_sorted.pop()
#             count += 1
#             # 원하는 index의 값까지 get()에 성공했을 경우 count 출력하고 종료
#             if(get_value[1] == m):
#                 print(count)
#                 break
#         # 우선도가 떨어지는 수일 경우, 다시 que에 추가
#         else: que.put(get_value)

# 큐 10845
# 양방향 큐 사용
# from collections import deque
# import sys

# input = sys.stdin.readline
# num = int(input())

# queue = deque()
# # queue = deque([])
# # print(queue)
# for _ in range(num):
#     command_list = list(map(str, input().split()))
#     # print("command_list :", command_list)
#     if(command_list[0] == 'push'):
#         queue.append(int(command_list[1]))
#         # print(command_list[1])
#     elif(command_list[0] == 'pop'):
#         if(len(queue) == 0): print(-1)
#         else:
#             pop_value = queue.popleft()
#             print(pop_value)
#     elif(command_list[0] == 'size'):
#         print(len(queue))
#     elif(command_list[0] == 'empty'):
#         if(len(queue) == 0): print(1)
#         else: print(0)
#     elif(command_list[0] == 'front'):
#         if(len(queue) == 0): print(-1)
#         else:
#             # pop_value = queue.popleft()
#             # print(pop_value)
#             # queue.appendleft(pop_value)
#             print(queue[0])
#     else: # back
#         if(len(queue) == 0): print(-1)
#         else:
#             # pop_value = queue.pop()
#             # print(pop_value)
#             # queue.append(pop_value)
#             print(queue[-1])


# 영화감독 숌
# from itertools import combinations

# num = int(input())
# i = 1
# while True:
#     i += 1
#     com = list(combinations())

# 비효율적이지만 10000 이하의 input이면 충분히 가능..할 듯
# 어떻게 하면 더 효율적으로 만들 수 있을까
# num = int(input())
# count = 0
# value = 665
# while True:
#     value += 1
    
#     if('666' in str(value)):
#         count += 1
#     if(count == num):
#         print(value)
#         break


# 요세푸스 11866
# from queue import Queue

# n, k = map(int, input().split())
# que = Queue()
# count = 0

# # 1부터 n까지 queue에 put()
# for i in range(1, n+1):
#     que.put(i)
# # print(que.queue)

# # 요세푸스 순열 list 생성
# Josephus_permutation_list = []
# while que.qsize():
#     count += 1
#     get_value = que.get()
#     if(count % k) == 0:
#         # print(get_value)
#         Josephus_permutation_list.append(get_value)
#     else: que.put(get_value)

# # 출력
# print("<", end= '')
# for i in range(n-1):
#     print("{0}, ".format(Josephus_permutation_list[i]), end= '')
# print(Josephus_permutation_list[-1], end='')
# print(">", end= '')


# 10828 스택
# import sys
# input = sys.stdin.readline

# command_num = int(input())
# # command_num 만큼의 명령어 입력받음
# stack_list = []
# for _ in range(command_num):
#     command_list = list(map(str, input().split()))
#     if(command_list[0] == 'push'):
#         stack_list.append(command_list[1])
#     elif(command_list[0] == 'pop'):
#         if(len(stack_list) == 0): print(-1)
#         else: print(stack_list.pop())
#     elif(command_list[0] == 'size'):
#         print(len(stack_list))
#     elif(command_list[0] == 'empty'):
#         if(len(stack_list) == 0): print(1)
#         else: print(0)
#     else: # top
#         if(len(stack_list) == 0): print(-1)
#         else: print(stack_list[-1])
        
#     # print("stack_list : ", stack_list)


# 10866 덱
# from collections import deque
# import sys
# input = sys.stdin.readline

# que = deque()

# command_num = int(input())
# for i in range(command_num):
#     command_list = list(map(str, input().split()))
#     if(command_list[0] == 'push_front'): que.appendleft(int(command_list[1]))
#     elif(command_list[0] == 'push_back'): que.append(int(command_list[1]))
#     elif(command_list[0] == 'pop_front'):
#         if(len(que) == 0): print(-1)
#         else: print(que.popleft())
#     elif(command_list[0] == 'pop_back'):
#         if(len(que) == 0): print(-1)
#         else: print(que.pop())

#     elif(command_list[0] == 'size'): print(len(que))
#     elif(command_list[0] == 'empty'):
#         if(len(que) == 0): print(1)
#         else: print(0)
#     elif(command_list[0] == 'front'):
#         if(len(que) == 0): print(-1)
#         else: print(que[0])
#     elif(command_list[0] == 'back'):
#         if(len(que) == 0): print(-1)
#         else: print(que[-1])


