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
# done

# num_of_toping = int(input())
# price_of_dough, price_of_toping = map(int, input().split())
# cal_of_dough = int(input())
# cal_of_toping_list = [int(input()) for _ in range(num_of_toping)]

# ans_cal = cal_of_dough
# ans_dol = price_of_dough
# max_cal_per_dol = ans_cal/ans_dol

# cal_of_toping_list.sort()
# cal_of_toping_list.reverse()
# # print(cal_of_toping_list)

# for i in range(num_of_toping):
#     if (ans_cal + cal_of_toping_list[i])/(ans_dol + price_of_toping) > (ans_cal/ans_dol):
#         ans_cal += cal_of_toping_list[i]
#         ans_dol += price_of_toping
#         max_cal_per_dol = ans_cal/ans_dol
#     else:
#         break

# print(int(max_cal_per_dol))


# 4040 펜션
# 5번 케이스가 뭐길래..
# days, rooms = map(int, input().split())
# rooms_plan = [list(str(input())) for _ in range(days)]
# # print(rooms_plan)
# start_day, leaving_day = map(int, input().split())

# index = start_day - 1   # index << days_index : 0 ~ 
# room_change_count = 0

# while True:
#     # while True:
#     # 그 날 가능한 방 목록들 추려내기
#     possible_rooms = [i for i in range(rooms) if rooms_plan[index][i] == 'O']
#     possible_rooms.reverse() # 효과 없음, 무 변화
#     # print(possible_rooms)
    
#     # 방이 없다면, 예약 불가
#     if(len(possible_rooms) == 0):
#         print("-1")
#         break
#     # 방이 있다면, 그 중에서 가장 빠른 방 번호 백업
#     else: backup_room_number = possible_rooms[0]

#     # greedy 접근, 가장 오래 머물 수 있는 곳 택1
#     # for i in range(start_day-1, leaving_day):
#     for i in range(index, leaving_day - 1):
#         for j in possible_rooms:
#             if(rooms_plan[i][j] == 'X'):
#                 possible_rooms.remove(j)    # 특정 요소 제거
        
#         if(len(possible_rooms) <= 1):
#             # print("index : ", index)
#             break

#         # 위 break 때 index가 증가되지 않은 상태여야 하므로 아래의 코드가 여기 있어야 함
#         # 여러 개의 방의 예약 가능 최종 날짜가 겹칠 수 있기 때문
#         index = i

#     # 그 방의 방 번호
#     if(len(possible_rooms)) == 1:           # 안 겹친 경우
#         room_number = possible_rooms[0]
#     else: room_number = backup_room_number  # 겹친 경우
 
#     # 가장 오래 머물 수 있는 room만 있음
#     # print(room_number)

#     # 그 방에서 하루 하루씩 있다가
#     for i in range(index, leaving_day-1):
#         # 오늘은 거기 못 있는 경우
#         if(rooms_plan[i][room_number]) == 'X':
#             break
#         # 오늘도 지내는 경우
#         else: index += 1

#     # (leaving_day-1)까지 펜션에서 잘 지냈거나 모자란 경우 다음방 탐색
#     if(index == (leaving_day-1)): #끝
#         print(room_change_count)
#         break
#     else:
#         # 다음방 탐색 → 반복
#         room_change_count += 1
#         continue


# https://0equal2.tistory.com/26
# n,m = map(int,input().split())


# # 2.
# info = [['X']*m] # 날짜를 편하게 확인하기 위해서 0번째 줄은 임의로 추가

# for i in range(n):
#     info.append(list(input()))
# print(info)

# # 3. 손님이 머물 날
# s, t = map(int, input().split())



# # 4.


# def check(n):

#     maxday=0

#     for i in range(m):
#         day=0
#         for j in range(n,t):
#             if info[j][i]=='O':
#                 day+=1
#             else:
#                 break

#         if maxday<day:
#             maxday=day
#     return maxday


# count=-1
# today=s

# while today<t:
    
#     stay=check(today)

#     if stay==0:
#         count=-1
#         break

#     # print(stay)
#     count+=1
#     today+=stay

# print(count)