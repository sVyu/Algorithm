# Bronze I
# 명령 프롬프트
# num = int(input())
# command_list = [list(str(input())) for _ in range(num)]
# result_command_list = command_list[0]

# for i in range(1, len(command_list)):
#     for j in range(0, len(command_list[i])):
#         if(command_list[i][j] != command_list[i-1][j]):
#             result_command_list[j] = '?'

# # print(result_command_list)
# for i in range(len(result_command_list)):
#     print(result_command_list[i], end='')


# n=int(input())
# m=[]
# for i in range(n):
#     a,b=map(int,input().split())
#     m.append([a,b])
#     m[i].append(m[i][1]+m[i][0])
# m.sort(key=lambda x: (x[2],x[1],x[0]))
# x=m[0][1]
# y=1
# for i in range(n):
#     if x<=m[i][0]:
#         x=m[i][1]
#         y+=1
# print(y)