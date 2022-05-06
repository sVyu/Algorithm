# 11052 카드 구매하기
# num = int(input())
# price_list = list(map(int, input().split()))

# max_price = 0
# max_ratio_index = 0
# ratio_list = [0] * num

# # 비율(개수/가격)을 책정한 list
# for i in range(len(price_list)):
#     ratio_list[i] = price_list[i]/(i+1)
# # print(ratio_list)

# def for_max_price(rest_price):
#     global max_ratio_index
#     global max_price

#     max_ratio_index = 0
#     # rest_price까지 가장 높은 ratio의 index 찾기
#     for i in range(rest_price):
#         if ratio_list[max_ratio_index] <= ratio_list[i]:
#             max_ratio_index = i

#     # price 합산
#     max_price += (rest_price // (max_ratio_index + 1)) * price_list[max_ratio_index]
#     rest_price %= (max_ratio_index + 1)
#     # print(max_ratio_index, max_price, rest_price)

#     # 아직 계산할 price가 남아있으면 추가 진행
#     if(rest_price != 0):
#         for_max_price(int(rest_price))

# for_max_price(num)
# print(max_price)

