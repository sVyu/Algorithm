# 2001 : 최소 대금
# num_list = [int(input()) for _ in range(5)]

# min_pasta = min(num_list[0:3])
# min_juice = min(num_list[3:])
# print("{0:.1f}".format(float(min_pasta + min_juice)*1.1))


# 3120 리모컨

# a, b = map(int, input().split())
# count = 0

## 33 11 → 4
## 22 3 → 3     이 맞는데 6 나옴

# while a != b:
#     gap = b - a
#     if(gap > 0):
#         if(gap >= 5):
#             if(gap >= 10):
#                 a += 10
#                 count += 1
#             else:   # 5, 6, 7, 8, 9
#                 if(gap >= 8):
                
#                 else:

#         else:
#             count += gap
#             break
#     elif(gap < 0):
#         if(gap <= -5):
#             if(gap <= -10):
#                 a -= 10
#                 count += 1
#             else:
#                 a -= 5
#                 count += 1
#         else:
#             count -= gap
#             break
#     else: # gap ==0
#         break
# print(count)

# try2
# a, b = map(int, input().split())
# gap = b - a
# count_list = [0]*8

# for()
# print(min(count_list))

# try3
# a, b = map(int, input().split())
# count = 0

# while a != b:
#     gap = b - a
#     # 절대값으로 10도 이상 차이가 나는 경우
#     if gap >= 10 :
#         a += 10
#         count += 1
#         continue
#     elif gap <= -10 :
#         a -= 10
#         count += 1
#         continue

#     abs_gap = abs(gap)
#     if (abs_gap == 9) :
#         count += 2
#         break
#     elif (abs_gap == 8):
#         count += 3
#         break
#     elif (abs_gap == 7):
#         count += 3
#         break
#     elif (abs_gap == 6):
#         count += 2
#         break
#     elif (abs_gap == 5):
#         count += 1
#         break
#     elif (abs_gap == 4):
#         count += 2
#         break
#     elif (abs_gap == 3):
#         count += 3
#         break
#     elif (abs_gap == 2):
#         count += 2
#         break
#     elif (abs_gap == 1):
#         count += 1
#         break
#     else: # abs_gap == 0
#         break

# print(count)


# 3301 거스름돈
# num = int(input())
# count = 0
# while num > 0:
#     if(num // 50000) > 0:
#         count += (num // 50000)
#         num %= 50000
#     elif(num // 10000) > 0:
#         count += (num // 10000)
#         num %= 10000
#     elif(num // 5000) > 0:
#         count += (num // 5000)
#         num %= 5000
#     elif(num // 1000) > 0:
#         count += (num // 1000)
#         num %= 1000
#     elif(num // 500) > 0:
#         count += (num // 500)
#         num %= 500
#     elif(num // 100) > 0:
#         count += (num // 100)
#         num %= 100
#     elif(num // 50) > 0:
#         count += (num // 50)
#         num %= 50
#     elif(num // 10) > 0:
#         count += (num // 10)
#         num %= 10

# print(count)


# 3321 최고의 피자
# 시간 초과
# num_of_toping = int(input())
# price_of_dough, price_of_toping = map(int, input().split())
# cal_of_dough = int(input())
# cal_of_toping_list = [int(input()) for _ in range(num_of_toping)]

# on_off_toping_list = [0] * num_of_toping
# max = 0

# for i in range(2**num_of_toping):
#     temp_i = i
#     index = -1

#     # i를 2진수 리스트 형태로 표현
#     while temp_i > 0:
#         on_off_toping_list[index] = temp_i % 2
#         temp_i //= 2
#         index -= 1  # 인덱스는 뒤에서부터 1씩 감소
#     # print(on_off_toping_list)

#     # 칼로리, 가격 합계 계산
#     cal_sum = cal_of_dough
#     price_sum = price_of_dough
#     for j in range(num_of_toping):
#         cal_sum += on_off_toping_list[j] * cal_of_toping_list[j]
#         price_sum += on_off_toping_list[j] * price_of_toping
    
#     # 새로운 최대값이 나왔을 시 갱신
#     if max < (cal_sum/price_sum):
#         print(on_off_toping_list)
#         max = cal_sum/price_sum
#         print(max)

# print(int(max))

# 분수로 접근해서 풀어보면 좋을 듯
