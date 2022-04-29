# # 2839 설탕 배달
# num = int(input())
# num_5kg = 0
# backup_num = num

# for i in range(num//5, -1, -1):
#     num_5kg = i
#     num = backup_num - num_5kg * 5
#     if(num % 3 == 0):
#         print(num_5kg + (num//3))
#         quit()
#     else: continue

# print(-1)


# 11399 ATM
# num = int(input())
# num_list = list(map(int, input().split()))
# num_list.sort()
# total_min, certain_index_min = 0, 0

# for i in range(len(num_list)):
#     certain_index_min += num_list[i]
#     total_min += certain_index_min

# print(total_min)


# 1931 회의실 배정
# num = int(input())
# num_list = [list(map(int, input().split())) for _ in range(num)]
# meeting_end_time = 0
# count = 0
# # 예시 데이터는 정렬한 걸 줬는데, 설명에는 정렬 데이터를 준다는 말이 없다
# num_list.sort(key=lambda x: (x[1], x[0]))

# for i in range(len(num_list)):
#     if(num_list[i][0] >= meeting_end_time):
#         meeting_end_time = num_list[i][1]
#         count += 1

# print(count)


# 1026 보물
num = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

new_a_list = [0] * num
c_list = [0] * num

a_list.sort(reverse=True)
# print(a_list)

# 조건 : b_list는 재배열하면 안 됨 → 하면 되게 쉬워짐
# 제일 작은 b_list index를 찾을 것
# 거기서부터 제일 큰 a_list 값을 할당할 것

for i in range(num):
    min = 101
    min_index = 0

    for j in range(len(b_list)):
        if(b_list[j] < min) & (c_list[j] == 0):
            min = b_list[j]
            min_index = j
    
    c_list[min_index] = 1
    new_a_list[min_index] = a_list[i]

sum = 0
for i in range(num):
    sum += new_a_list[i] * b_list[i]

# print(new_a_list)
print(sum)