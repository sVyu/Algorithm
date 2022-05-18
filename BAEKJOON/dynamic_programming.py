# 11052 카드 구매하기
# num = int(input())
# price_list = list(map(float, input().split()))
# print(price_list)

# sum_price = 0
# ratio_list = [0] * num

# # 비율(개수/가격)을 책정한 list
# for i in range(len(price_list)):
#     ratio_list[i] = price_list[i]/(i+1)
# # print(ratio_list)

# def for_sum_price(rest_price):
#     # global max_ratio_index
#     global sum_price

#     max_ratio_index = 0
#     # rest_price까지 가장 높은 ratio의 index 찾기
#     # for i in range(rest_price+1):
#     for i in range(rest_price):
#         if ratio_list[max_ratio_index] <= ratio_list[i]:
#             max_ratio_index = i

#     # price 합산
#     # sum_price += (rest_price // (max_ratio_index + 1)) * price_list[max_ratio_index]
#     # rest_price %= (max_ratio_index + 1)
#     temp_price = (rest_price // (max_ratio_index + 1)) * price_list[max_ratio_index]
#     sum_price += temp_price
#     # rest_price = rest_price - (rest_price // (max_ratio_index+1))
#     rest_price %= (max_ratio_index + 1)
#     print(max_ratio_index, sum_price, "rest_price :",rest_price)

#     # 아직 계산할 price가 남아있으면 추가 진행
#     if(rest_price != 0):
#         # for_sum_price(int(rest_price))
#         for_sum_price((rest_price))

# for_sum_price(num)
# print(sum_price)


# num = int(input())
# price_list = list(map(int, input().split()))
# price_list.insert(0, 0)
# # print(price_list)

# dp_list = [0] * (num+1)
# for i in range(1, num+1):
#     for j in range(1, i+1):
#         dp_list[i] = max(dp_list[i], price_list[j] + dp_list[i-j])

# # print(dp_list)
# print(dp_list[num])


# 1463 1로 만들기
# num = int(input())

# # 0, 1, 2, ... 를 이용해서 1을 만드는 최소한의 횟수
# num_list = [0, 0, 1, 1]
# for i in range(4, num+1):
#     min_list = []
#     if(i % 3 == 0):
#         min_list.append(num_list[i//3]+1)
#     if(i % 2 == 0):
#         min_list.append(num_list[i//2]+1)
#     min_list.append(num_list[i-1]+1)
#     # print(i, min_list)
#     num_list.append(min(min_list))
# print(num_list[num])

# 확인용 코드
# for i in range(len(num_list)):
#     print(i, num_list[i])


# while num != 1:
#     if(num % 3 == 0):
#         num //= 3
#     elif(num % 2 == 0):
#         num //= 2
#     else:
#         num -= 1
    
#     count += 1
#     print("num : ", num)

# print(count)

# 결과값
#10
# num :  5
# num :  4
# num :  2
# num :  1
# 4



# 9095 1,2,3 더하기
# n = int(input())
# num_list = [int(input()) for _ in range(n)]

# number_of_cases_list = [0, 1, 2, 4]

# for i in range(4, 11):
#     number_of_cases_list.append(number_of_cases_list[i-1] + number_of_cases_list[i-2] + number_of_cases_list[i-3])

# for i in num_list:
#     print(number_of_cases_list[i])



# 1003 피보나치 함수
# n = int(input())
# num_list = [int(input()) for _ in range(n)]

# # enl : executed_number_list, (0, 1)이호출된 회수를 저장한 list
# enl = [[1,0], [0,1]]
# for i in range(41):
#     enl.append([enl[-2][0] + enl[-1][0], enl[-2][1] + enl[-1][1]])

# # for i in range(len(enl)):
# #     print(i, enl[i])

# for i in num_list:
#     print(enl[i][0], enl[i][1])


# 1932 정수 삼각형
# triangle_height = int(input())
# num_list = [list(map(int, input().split())) for _ in range(triangle_height)]
# # print(num_list)
# sum_list = [[0] * triangle_height for _ in range(triangle_height)]
# # print(sum_list)

# for i in range(triangle_height):
#     if(i == 0):
#         sum_list[0][0] = num_list[0][0]
#     elif(i == 1):
#         sum_list[1][0] = sum_list[0][0] + num_list[1][0]
#         sum_list[1][1] = sum_list[0][0] + num_list[1][1]
#     else:
#         for j in range(i+1):
#             if(j == 0):
#                 sum_list[i][0] = sum_list[i-1][0] + num_list[i][0]
#             elif(j == i):
#                 sum_list[i][j] = sum_list[i-1][j-1] + num_list[i][j]
#             else:
#                 max_sum = [sum_list[i-1][j-1], sum_list[i-1][j]]
#                 sum_list[i][j] = max(max_sum) + num_list[i][j]

# # for i in range(triangle_height):
# #     print(i, sum_list[i])

# print(max(sum_list[triangle_height-1]))


# 11053 가장 긴 증가하는 부분수열
# list_length = int(input())
# num_list = list(map(int, input().split()))
# dp_list = [1] * list_length
# # print(dp_list)

# for i in range(1, list_length):
#     for j in range(i):
#         if((num_list[i] > num_list[j]) & (dp_list[i] == dp_list[j])):
#             dp_list[i] += 1
# # print(dp_list)
# print(max(dp_list))


# 11722 가장 긴 감소하는 부분수열
# list_length = int(input())
# num_list = list(map(int, input().split()))
# dp_list = [1] * list_length
# # print(dp_list)

# for i in range(1, list_length):
#     for j in range(i):
#         if((num_list[i] < num_list[j]) & (dp_list[i] == dp_list[j])):
#             dp_list[i] += 1
# # print(dp_list)
# print(max(dp_list))


# 11054 가장 긴 바이토닉 부분수열
# import sys

# list_length = int(input())
# num_list = list(map(int, sys.stdin.readline().split()))

# dp_list_inc = [1] * list_length # 증가 dp
# dp_list_dec = [1] * list_length # 감소 dp

# # 증가하는 부분
# for i in range(1, list_length): # 체크 할 수
#     for j in range(i): # 비교하는 수
#         # 체크하는 자리 인덱스가 비교하는 수보다 크고 dp가 같다면 +1
#         if((num_list[i] > num_list[j]) & (dp_list_inc[i] == dp_list_inc[j])):
#             dp_list_inc[i] += 1
# # print(dp_list_inc)

# # 감소하는 부분, 뒤에서부터
# for i in range(list_length-2, -1, -1):
#     for j in range(list_length-1, i, -1):
#         if((num_list[i] > num_list[j]) & (dp_list_dec[i] == dp_list_dec[j])):
#             dp_list_dec[i] += 1
# # print(dp_list_dec)

# # 각각의 증가 감소 리스트의 합 -1
# new_dp_list = [(dp_list_inc[i] + dp_list_dec[i] - 1) for i in range(list_length)]

# print(max(new_dp_list))


# 1495 기타리스트
# 메모리 초과.. → 리스트 not in 으로 해결
# n, s, m = map(int, input().split())
# vol_list = list(map(int, input().split()))

# pos_vol_list = [s]

# # 0부터 n-1까지 볼륨 조절 start
# for i in range(n):
#     # 가능한 볼륨 리스트의 길이가 0이면 print("-1") 하고 종료
#     pos_vol_list_len = len(pos_vol_list)
#     new_pos_vol_list = []

#     if(pos_vol_list_len == 0):
#         print("-1")
#         quit()

#     for j in range(pos_vol_list_len):
#         if(0 <= (pos_vol_list[j] - vol_list[i]) <= m):
#             if(pos_vol_list[j] - vol_list[i] not in new_pos_vol_list):
#                 new_pos_vol_list.append(pos_vol_list[j] - vol_list[i])
#         if(0 <= (pos_vol_list[j] + vol_list[i]) <= m):
#             if(pos_vol_list[j] + vol_list[i] not in new_pos_vol_list):
#                 new_pos_vol_list.append(pos_vol_list[j] + vol_list[i])
    
#     # pos_vol_list 갱신
#     # pos_vol_list = pos_vol_list[pos_vol_list_len:]
#     pos_vol_list = new_pos_vol_list
#     # print(i, pos_vol_list)

# # vol_list[n-1] 번째 계산 이후에도 확인을 해주어야 함
# if(len(pos_vol_list) == 0):
#     print("-1")
#     quit()
# else: print(max(pos_vol_list))


