# 13460 구슬 탈출2
# import sys
# input = sys.stdin.readline
# from collections import deque

# def solve():
#     N, M = map(int, input().split())
#     board = [list(input().rstrip()) for _ in range(N)]
#     R_xy, B_xy = -1, -1
#     # R, B 시작 위치 저장
#     for x in range(N):
#         for y in range(M):
#             if board[x][y] == 'R':
#                 R_xy = [x, y]
#                 board[x][y] = '.'
#             elif board[x][y] == 'B':
#                 B_xy = [x, y]
#                 board[x][y] = '.'
#         # print(board[x])
#     inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

#     # RB 위치 중복 파악을 위한 set
#     que = deque([[0, R_xy, B_xy]])
#     RB_xy_set = set()
#     RB_xy_set.add(tuple([tuple(R_xy), tuple(B_xy)]))

#     while True:
#         # print(que)
#         cnt, R_xy, B_xy = que.popleft()
#         if cnt >= 10:
#             print(-1)
#             break

#         for plus_x, plus_y in inc_xy:
#             tmp_R_xy, tmp_B_xy = R_xy.copy(), B_xy.copy()
#             # print("std", tmp_R_xy, tmp_B_xy)
#             R_blocked, B_blocked = False, False

#             while not R_blocked or not B_blocked:
#                 # print("[2]", cnt, R_xy, B_xy, tmp_R_xy, tmp_B_xy, plus_x, plus_y, R_blocked, B_blocked)
#                 can_R_move = False
#                 if not R_blocked:
#                     if board[tmp_R_xy[0]+plus_x][tmp_R_xy[1]+plus_y] == '#':
#                         R_blocked = True
#                     elif board[tmp_R_xy[0]+plus_x][tmp_R_xy[1]+plus_y] == '.':
#                         if tmp_R_xy[0]+plus_x == tmp_B_xy[0] and tmp_R_xy[1]+plus_y == tmp_B_xy[1]:
#                             # print("haha")
#                             if not B_blocked:
#                                 can_R_move = True
#                         else:
#                             tmp_R_xy[0] += plus_x
#                             tmp_R_xy[1] += plus_y
#                     else: # O
#                         if cnt + 1 <= 10:
#                             print(cnt+1)
#                             return

#                 # R_blocked 처리해야함
#                 if not B_blocked:
#                     if board[tmp_B_xy[0]+plus_x][tmp_B_xy[1]+plus_y] == '#':
#                         B_blocked = True
#                         if can_R_move:
#                             R_blocked = True
#                     elif board[tmp_B_xy[0]+plus_x][tmp_B_xy[1]+plus_y] == '.':
#                         if tmp_B_xy[0]+plus_x == tmp_R_xy[0] and tmp_B_xy[1]+plus_y == tmp_R_xy[1]:
#                             B_blocked = True
#                             break
#                         # board[tmp_B_xy[0]][tmp_B_xy[1]] = '.'
#                         tmp_B_xy[0] += plus_x
#                         tmp_B_xy[1] += plus_y
#                         # board[tmp_B_xy[0]][tmp_B_xy[1]] = 'B'
#                         if can_R_move:
#                             # board[tmp_R_xy[0]][tmp_R_xy[1]] = '.'
#                             tmp_R_xy[0] += plus_x
#                             tmp_R_xy[1] += plus_y
#                             # board[tmp_R_xy[0]][tmp_R_xy[1]] = 'R'
#                     else: # O : 구멍에 빠짐
#                         break
                
#                 # for x in range(N):
#                 #     print(board[x])
#                 # print()
#             # while문 종료
#             print("while", cnt, plus_x, plus_y, tmp_R_xy, tmp_B_xy)
#             print()

#             # 해당 위치에 대한 정보가 set에 없는 경우
#             if tuple([tuple(tmp_R_xy), tuple(tmp_B_xy)]) not in RB_xy_set:
#                 que.append([cnt+1, tmp_R_xy, tmp_B_xy])
#                 print("que", que)

# solve()


# try 2
# import sys
# input = sys.stdin.readline
# from collections import deque

# def solve():
#     N, M = map(int, input().split())
#     board = [list(input().rstrip()) for _ in range(N)]
#     R_x, R_y, B_x, B_y = -1, -1, -1, -1
#     # R, B 시작 위치 저장
#     for x in range(N):
#         for y in range(M):
#             if board[x][y] == 'R':
#                 R_x, R_y = [x, y]
#                 board[x][y] = '.'
#             elif board[x][y] == 'B':
#                 B_x, B_y = [x, y]
#                 board[x][y] = '.'
#         # print(board[x])
#     inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

#     # RB 위치 중복 파악을 위한 set
#     que = deque([[0, R_x, R_y, B_x, B_y]])
#     RB_xy_set = set()
#     RB_xy_set.add(tuple([R_x, R_y, B_x, B_y]))

#     while que:
#         # print(que)
#         cnt, R_x, R_y, B_x, B_y = que.popleft()
#         if cnt >= 10:
#             break
        
#         for plus_x, plus_y in inc_xy:
#             tmp_R_x, tmp_R_y, tmp_B_x, tmp_B_y = R_x, R_y, B_x, B_y
#             # print("std", tmp_R_xy, tmp_B_xy)
#             R_blocked, B_blocked = False, False
#             R_O_check, B_O_check = False, False

#             # 구슬이 아직 움직여지면
#             while not (R_blocked or R_O_check) or not (B_blocked or B_O_check):
#                 # print("[2]", cnt, tmp_R_x, tmp_R_y, tmp_B_x, tmp_B_y, plus_x, plus_y, R_blocked, B_blocked)
#                 can_R_move = False
#                 # R에 대해 벽에 막히지 않고, O에 빠지지 않았으면
#                 if not (R_blocked or R_O_check):
#                     # 벽이면
#                     if board[tmp_R_x + plus_x][tmp_R_y + plus_y] == '#':
#                         R_blocked = True
#                     # . 이면 (B 위치일수도 있으니 확인)
#                     elif board[tmp_R_x + plus_x][tmp_R_y + plus_y] == '.':
#                         if tmp_R_x + plus_x == tmp_B_x and tmp_R_y + plus_y == tmp_B_y:
#                             # print("haha")
#                             if not B_blocked:
#                                 can_R_move = True
#                             else: # B_blocked
#                                 R_blocked = True
#                         else:
#                             tmp_R_x += plus_x
#                             tmp_R_y += plus_y
#                     else: # O
#                         R_O_check = True
#                         tmp_R_x, tmp_R_y = -1, -1

#                 # R_blocked 처리해야함
#                 if not (B_blocked or B_O_check):
#                     if board[tmp_B_x + plus_x][tmp_B_y + plus_y] == '#':
#                         B_blocked = True
#                         if can_R_move:
#                             R_blocked = True
#                     elif board[tmp_B_x + plus_x][tmp_B_y + plus_y] == '.':
#                         if tmp_B_x + plus_x == tmp_R_x and tmp_B_y + plus_y == tmp_R_y:
#                             B_blocked = True
#                             break

#                         tmp_B_x += plus_x
#                         tmp_B_y += plus_y
#                         if can_R_move:
#                             tmp_R_x += plus_x
#                             tmp_R_y += plus_y
#                     else: # O : 구멍에 빠짐
#                         B_O_check = True
#                         tmp_B_x, tmp_B_y = -1, -1

#                 # for x in range(N):
#                 #     print(board[x])
#                 # print()
#             # while문 종료
#             # print("while", cnt, "plus_xy", plus_x, plus_y, "xy", tmp_R_x, tmp_R_y, tmp_B_x, tmp_B_y)
#             if B_O_check:
#                 continue

#             if R_O_check: # not B_O_check
#                 print(cnt+1)
#                 return

#             # 해당 위치에 대한 정보가 set에 없는 경우
#             if tuple([tmp_R_x, tmp_R_y, tmp_B_x, tmp_B_y]) not in RB_xy_set:
#                 RB_xy_set.add(tuple([tmp_R_x, tmp_R_y, tmp_B_x, tmp_B_y]))
#                 que.append([cnt+1, tmp_R_x, tmp_R_y, tmp_B_x, tmp_B_y])
#         #         print("que", que)
#         # print()
#     print(-1)

# solve()


# 14503 로봇 청소기
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# r, c, d = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# dict_d = dict({0:[-1, 0], 1:[0, 1], 2:[1, 0], 3:[0, -1]})

# x, y = r, c
# ans = 0

# while True:
#     found_check = False
    
#     # 1. 현재 위치 청소
#     if board[x][y] == 0:
#         board[x][y] = 2
#         ans += 1
    
#     # print(x, y, d)
#     # for k in range(N):
#     #     print(board[k])
#     # print()

#     # 2.1.  2.2.
#     for _ in range(4):
#         d = (d-1) % 4
#         nx, ny = x + dict_d[d][0], y + dict_d[d][1]
        
#         if board[nx][ny] == 0:
#             found_check = True
#             x, y = nx, ny
#             break
    
#     # 청소할 공간 찾은 경우 continue해서 다시 1번부터
#     if found_check:
#         continue

#     # not found_check (네 방향 다 봐도 청소할 공간이 없는 경우)
#     nx, ny = x - dict_d[d][0], y - dict_d[d][1]
#     if 0 <= nx < N and 0 <= ny < M:
#         # 뒷칸이 벽이 아니면 후진
#         if board[nx][ny] != 1:
#             x, y = nx, ny
#         else: # 1 즉, 벽이면 break
#             break

# print(ans)

# 12100 2048(Easy)
# 9:41 pm ~ 10:25

# import sys
# input = sys.stdin.readline
# from collections import deque

# # cnt는 최대 5번까지
# def backtracking(N, board, cnt):
#     global max_block
#     que = deque()

#     cnt += 1
#     # 0 북, 1 동, 2 남 3 서
#     for d in range(4):
#         next_board = [[0] * N for _ in range(N)]
#         for x in range(N):
#             next_board[x] = board[x][:]

#         # 북쪽
#         if d == 0:
#             for y in range(N):
#                 pre_x_val = -1
#                 for x in range(N):
#                     # 블록 숫자 합치기부터
#                     if next_board[x][y] != 0:
#                         if pre_x_val == -1:
#                             pre_x_val = next_board[x][y]
#                         else:
#                             if pre_x_val == next_board[x][y]:
#                                 que.append(pre_x_val*2)
#                                 # next_board[pre_x_idx] *= 2
#                                 pre_x_val = -1
#                             else:
#                                 que.append(pre_x_val)
#                                 pre_x_val = next_board[x][y]
#                         next_board[x][y] = 0

#                 if pre_x_val != -1:
#                     que.append(pre_x_val)

#                 # 위에서부터 하나씩 put
#                 for x in range(len(que)):
#                     val = que.popleft()
#                     if max_block < val:
#                         max_block = val
#                     next_board[x][y] = val

#         # 동쪽
#         elif d == 1:
#             for x in range(N):
#                 pre_x_val = -1
#                 for y in range(N-1, -1, -1):
#                     # 블록 숫자 합치기부터
#                     if next_board[x][y] != 0:
#                         if pre_x_val == -1:
#                             pre_x_val = next_board[x][y]
#                         else:
#                             if pre_x_val == next_board[x][y]:
#                                 que.append(pre_x_val*2)
#                                 # next_board[pre_x_idx] *= 2
#                                 pre_x_val = -1
#                             else:
#                                 que.append(pre_x_val)
#                                 pre_x_val = next_board[x][y]
#                         next_board[x][y] = 0

#                 if pre_x_val != -1:
#                     que.append(pre_x_val)

#                 # 위에서부터 하나씩 put
#                 for y in range(N-1, N-1-len(que), -1):
#                     val = que.popleft()
#                     if max_block < val:
#                         max_block = val
#                     next_board[x][y] = val

#         # 남쪽
#         elif d == 2:
#             for y in range(N):
#                 pre_x_val = -1
#                 for x in range(N-1, -1, -1):
#                     # 블록 숫자 합치기부터
#                     if next_board[x][y] != 0:
#                         if pre_x_val == -1:
#                             pre_x_val = next_board[x][y]
#                         else:
#                             if pre_x_val == next_board[x][y]:
#                                 que.append(pre_x_val*2)
#                                 # next_board[pre_x_idx] *= 2
#                                 pre_x_val = -1
#                             else:
#                                 que.append(pre_x_val)
#                                 pre_x_val = next_board[x][y]
#                         next_board[x][y] = 0

#                 if pre_x_val != -1:
#                     que.append(pre_x_val)

#                 # 위에서부터 하나씩 put
#                 for x in range(N-1, N-1-len(que), -1):
#                     val = que.popleft()
#                     if max_block < val:
#                         max_block = val
#                     next_board[x][y] = val
    
#         # 서쪽
#         else: # d == 3:
#             for x in range(N):
#                 pre_x_val = -1
#                 for y in range(N):
#                     # 블록 숫자 합치기부터
#                     if next_board[x][y] != 0:
#                         if pre_x_val == -1:
#                             pre_x_val = next_board[x][y]
#                         else:
#                             if pre_x_val == next_board[x][y]:
#                                 que.append(pre_x_val*2)
#                                 # next_board[pre_x_idx] *= 2
#                                 pre_x_val = -1
#                             else:
#                                 que.append(pre_x_val)
#                                 pre_x_val = next_board[x][y]
#                         next_board[x][y] = 0

#                 if pre_x_val != -1:
#                     que.append(pre_x_val)

#                 # 위에서부터 하나씩 put
#                 for y in range(len(que)):
#                     val = que.popleft()
#                     if max_block < val:
#                         max_block = val
#                     next_board[x][y] = val

#         # print(cnt, d)
#         # for x in range(N):
#         #     print(next_board[x])
#         # print()
#         # input()

#         if cnt < 5:
#             backtracking(N, next_board, cnt)

            
# def solve():
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     global max_block
#     max_block = 0

#     backtracking(N, board, 0)
#     print(max_block)

# solve()

# a = [0, 0, 0, 0]
# b = [0, 1, 2, 3]
# a = b[:]
# print(a)



# 14500 테트로미노
# 09:16 pm ~ 09:53 pm
# 09:45 제출(시간 초과)
# PyPy3로 제출하니 통과

# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]

# max_val = 0
# # 1자 가로, 세로
# for x in range(N):
#     for y in range(M-3):
#         sum_val = sum(board[x][y:y+4])
#         # sum_val = 0
#         # for k in range(4):
#         #     sum_val += board[x][y+k] 

#         if max_val < sum_val:
#             max_val = sum_val
#             # print("[1]", max_val, x, y)
#             # input()

# for y in range(M):
#     for x in range(N-3):
#         sum_val = 0
#         for k in range(4):
#             sum_val += board[x+k][y] 
#         if max_val < sum_val:
#             max_val = sum_val
#             # print("[2]", max_val, x, y)
#             # input()            

# # 네모
# for x in range(N-1):
#     for y in range(M-1):
#         sum_val = 0
#         sum_val += board[x][y] + board[x][y+1] + board[x+1][y] + board[x+1][y+1]
#         if max_val < sum_val:
#             max_val = sum_val
#             # print("[3]", max_val, x, y)
#             # input()

# # 6칸 2x3
# # L, Z, 'ㅗ' block
# block = [[1,1,1,1,0,0], [1,1,1,0,0,1], [1,0,0,1,1,1], [0,0,1,1,1,1],
#         [0,1,1,1,1,0], [1,1,0,0,1,1],
#         [0,1,0,1,1,1], [1,1,1,0,1,0]
# ]

# for x in range(N-1):
#     for y in range(M-2):
#         for k in range(8):
#             sum_val = 0
#             block_idx = 0
#             for kx in range(2):
#                 for ky in range(3):
#                     sum_val += board[x + kx][y + ky] * block[k][block_idx]
#                     block_idx += 1
#             # print(x, y, k, sum_val)

#             if max_val < sum_val:
#                 max_val = sum_val
#                 # print("[4]", max_val, x, y)
#                 # input()

# # 6칸 3x2
# block = [[1,0,1,0,1,1], [1,1,1,0,1,0], [1,1,0,1,0,1], [0,1,0,1,1,1],
#         [1,0,1,1,0,1], [0,1,1,1,1,0],
#         [1,0,1,1,1,0], [0,1,1,1,0,1]
# ]

# for x in range(N-2):
#     for y in range(M-1):
#         for k in range(8):
#             sum_val = 0
#             block_idx = 0
#             for kx in range(3):
#                 for ky in range(2):
#                     sum_val += board[x + kx][y + ky] * block[k][block_idx]
#                     block_idx += 1

#             if max_val < sum_val:
#                 max_val = sum_val
#                 # print("[5]", max_val, x, y)
#                 # input()
# print(max_val)


# 14890 경사로
# pm 09:58 ~ 10:36

# import sys
# input = sys.stdin.readline

# N, L = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]

# ans = 0
# # 가로
# for x in range(N):
#     possible_check = True
#     stair_check = [False] * N

#     for y in range(N-1):
#         if not possible_check:
#             break

#         # 1칸 낮은 경우
#         if board[x][y] == board[x][y+1]+1:
#             # 경사로 놓을 칸까지 확보가 된 경우
#             if y+L < N:
#                 for k in range(L):
#                     if not stair_check[y+1+k]:
#                         stair_check[y+1+k] = True
#                     else:
#                         possible_check = False
#                         break
#             # 칸 부족
#             else:
#                 possible_check = False
#                 break
        
#         # 1칸 높은 경우
#         elif board[x][y] == board[x][y+1]-1:
#             # 경사로 놓을 칸까지 확보가 된 경우
#             if y+1-L >= 0:
#                 for k in range(L):
#                     if not stair_check[y-k]:
#                         stair_check[y-k] = True
#                     else:
#                         possible_check = False
#                         break
#             # 칸 부족
#             else:
#                 possible_check = False
#                 break

#         elif board[x][y] == board[x][y+1]:
#             continue
#         # 2층 이상 차이나는 경우
#         else:
#             possible_check = False
#             break

#     if possible_check:
#         ans += 1

# # 세로
# for y in range(N):
#     possible_check = True
#     stair_check = [False] * N

#     for x in range(N-1):
#         if not possible_check:
#             break

#         # 1칸 낮은 경우
#         if board[x][y] == board[x+1][y]+1:
#             # 경사로 놓을 칸까지 확보가 된 경우
#             if x+L < N:
#                 for k in range(L):
#                     if not stair_check[x+1+k]:
#                         stair_check[x+1+k] = True
#                     else:
#                         possible_check = False
#                         break
#             # 칸 부족
#             else:
#                 possible_check = False
#                 break
        
#         # 1칸 높은 경우
#         elif board[x][y] == board[x+1][y]-1:
#             # 경사로 놓을 칸까지 확보가 된 경우
#             if x+1-L >= 0:
#                 for k in range(L):
#                     if not stair_check[x-k]:
#                         stair_check[x-k] = True
#                     else:
#                         possible_check = False
#                         break
#             # 칸 부족
#             else:
#                 possible_check = False
#                 break

#         elif board[x][y] == board[x+1][y]:
#             continue
#         # 2층 이상 차이나는 경우
#         else:
#             possible_check = False
#             break

#     if possible_check:
#         ans += 1

# print(ans)


# 14891 톱니바퀴
# pm 10:45 ~ 11:19
# 1st -> 런타임에러 -> ans 계산 과정에도 %8
# 2nd -> 성공

# import sys
# input = sys.stdin.readline
# from collections import deque

# # N극 : 0, S극 : 1
# wheel = [list(map(int, str(input().rstrip()))) for _ in range(4)]
# # print(wheel)
# wheel_d = [0, 0, 0, 0]

# que = deque()

# for _ in range(int(input())):
#     num, di = map(int, input().split())
#     num -= 1

#     visited = [False] * 4
#     visited[num] = True
#     que.append([num, (-1)*di])
#     que_update = [0, 0, 0, 0]

#     # 어딜 돌려야하는지 체크 -> que
#     while que:
#         n, di = que.popleft()
#         que_update[n] = di

#         for plus_val in [1, -1]:
#             nn = n + plus_val
#             if 0 <= nn < 4 and not visited[nn]:
#                 if plus_val == 1:
#                     # 같은 극인 경우,
#                     if wheel[n][(wheel_d[n]+2)%8] == wheel[nn][(wheel_d[nn]+6)%8]:
#                         continue
#                     # 다른 극인 경우
#                     else:
#                         visited[nn] = True
#                         que.append([nn, (-1)*di])
#                 else: # plus_val == -1:
#                     if wheel[n][(wheel_d[n]+6)%8] == wheel[nn][(wheel_d[nn]+2)%8]:
#                         continue
#                     # 다른 극인 경우
#                     else:
#                         visited[nn] = True
#                         que.append([nn, (-1)*di])

#     # 하나씩 돌려서 확인
#     # print(que_update)
#     for x in range(4):
#         wheel_d[x] += que_update[x]
#     # print(wheel_d)

# ans = 0
# plus_val = 1
# for x in range(4):
#     if wheel[x][wheel_d[x]%8] == 1:
#         ans += plus_val
#     plus_val *= 2
# print(ans)


# 15683 감시
# import sys
# input = sys.stdin.readline
# from collections import deque

# def backtracking(N, M, board, cctv, cnt, cnt_limit):
#     global min_blind_spot

#     # 위, 오른쪽, 밑, 왼쪽
#     d = [0, 1, 2, 3]
#     d_cctv = [[0, 1], [1, 0], [0, -1], [-1, 0]]

#     dot_x, dot_y, cctv_num = cctv[cnt]
#     cnt += 1
#     que = deque()

#     # 2번은 나올 수 있는 패턴이 2가지 5번은 1가지 경우밖에 없으므로
#     d_limit = 4
#     if cctv_num == 2:
#         d_limit = 2
#     elif cctv_num == 5:
#         d_limit = 1

#     # k는 cctv 방향인 n에 대해 +할 값
#     if cctv_num == 1:
#         list_k = [0]
#     elif cctv_num == 2:
#         list_k = [0, 2]
#     elif cctv_num == 3:
#         list_k = [0, 1]
#     elif cctv_num == 4:
#         list_k = [0, 1, 2]
#     else:
#         list_k = [0, 1, 2, 3]


#     for n in range(d_limit):
#         # 각 방향마다 기존 board를 복사해서 처리해야 함
#         copied_board = [[] for _ in range(N)]
#         for x in range(N):
#             copied_board[x] = board[x][:]

#         for k in list_k:
#             dd = d[(n+k)%4]
#             nx, ny = dot_x + d_cctv[dd][0], dot_y + d_cctv[dd][1]
#             if 0 <= nx < N and 0 <= ny < M and copied_board[nx][ny] != 6:
#                 que.append([nx, ny, cctv_num, dd])
        
#         # cctv 조건에 맞게 감시한 부분들 표시
#         while que:
#             x, y, cctv_num, dd = que.popleft()
#             # print(x, y, cctv_num, dd)
#             if copied_board[x][y] == 0:
#                 copied_board[x][y] = '#'
#             nx, ny = x + d_cctv[dd][0], y + d_cctv[dd][1]
#             if 0 <= nx < N and 0 <= ny < M and copied_board[nx][ny] != 6:
#                 que.append([nx, ny, cctv_num, dd])

#         # 아직 모든 cctv에 대해서 # 처리가 되지 않았으면 재귀를 더 진행
#         if cnt < cnt_limit:
#             backtracking(N, M, copied_board, cctv, cnt, cnt_limit)
#         else: # 조건 충족
#             blind_spot = 0
#             for x in range(N):
#                 for y in range(M):
#                     if copied_board[x][y] == 0:
#                         blind_spot += 1
#             if min_blind_spot > blind_spot:
#                 min_blind_spot = blind_spot
#                 # for x in range(N):
#                 #     print(copied_board[x])

#     # backtracking을 위한 cnt -= 1
#     cnt -= 1

# def solve():
#     N, M = map(int, input().split())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     cctv = []
#     for x in range(N):
#         for y in range(M):
#             if board[x][y] != 0 and board[x][y] != 6:
#                 cctv.append([x, y, board[x][y]])
#     # print(cctv)

#     global min_blind_spot
#     min_blind_spot = 64

#     copied_board = [[] for _ in range(N)]
#     for x in range(N):
#         copied_board[x] = board[x][:]
#     # print(copied_board)

#     # cctv가 없는 경우
#     if len(cctv) == 0:
#         wall = 0
#         for x in range(N):
#             for y in range(M):
#                 if board[x][y] == 6:
#                     wall += 1
#         print(N*M - wall)
#     else:
#         backtracking(N, M, copied_board, cctv, 0, len(cctv))
#         print(min_blind_spot)

# solve()


# 15684 사다리 조작
# pm 01:47 ~ 02:48 ~ 03:54
# 9퍼 시간 초과 02:48
# 11퍼 틀렸습니다 -> 반례 직접 찾음
# 결국 성공
'''
2 2 3
1 1 
2 1
정답 : 0
출력 : -1
'''

# import sys
# input = sys.stdin.readline

# # 사다리 타기로 전체 i에 대해 i to i가 되는지 체크
# def i_to_i(N, H, ladder):
#     pos_check = True
#     for i in range(1, N+1):
#         res_i = i
#         for res_x in range(1, H+1):
#             if ladder[res_x][res_i] != 0:
#                 res_i = ladder[res_x][res_i]
#         if res_i != i:
#             pos_check = False
#             break
#     return pos_check

# # backtracking()
# def btr(N, H, ladder, plus, plus_limit):
#     # copied_ladder = ladder.copy()
#     copied_ladder = [[] for _ in range(H+1)]
#     for x in range(1, H+1):
#         copied_ladder[x] = ladder[x][:]
#     plus += 1

#     global ans

#     # 브루트포스로 사다리 놓기
#     for x in range(1, H+1):
#         for y in range(1, N):
#             if ans != -1:
#                 return
#             if copied_ladder[x][y] == 0:
#                 # 사다리가 연속되는 경우
#                 if copied_ladder[x][y+1] != 0:
#                     continue
#                 # 아닌 경우(새로 놓을 수 있는 경우)
#                 else:
#                     copied_ladder[x][y] = y+1
#                     copied_ladder[x][y+1] = y
                
#                     # 사다리 개수를 아직 더 놓을 수 있는 경우
#                     if plus < plus_limit:
#                         btr(N, H, copied_ladder, plus, plus_limit)
#                     # limit 최대치인 경우(갈 수 있나 확인)
#                     else:
#                         # print(x, y)
#                         # for kx in range(1, H+1):
#                         #     print(copied_ladder[kx])
#                         # print()

#                         if i_to_i(N, H, copied_ladder):
#                             # print("ans", plus_limit)
#                             ans = plus_limit
#                             return

#                     # 백트래킹
#                     copied_ladder[x][y] = 0
#                     copied_ladder[x][y+1] = 0

#     # print()

# def solve():
#     N, M, H = map(int, input().split())
#     # ladder = [defaultdict(int) for _ in range(H+1)]
#     ladder = [[0]*(N+1) for _ in range(H+1)]
#     for _ in range(M):
#         a, b = map(int, input().split())
#         ladder[a][b] = b+1
#         ladder[a][b+1] = b

#     global ans
#     ans = -1

#     if i_to_i(N, H, ladder):
#         print(0)
#     else:
#         for plus_limit in range(1, 4):
#             btr(N, H, ladder, 0, plus_limit)
#         print(ans)

# solve()


# 15685 드래곤 커브
# pm 06:20 ~  07:00
# N = int(input())
# board = [[0]*101 for _ in range(101)]

# dragon_curve = [[0]]
# for _ in range(10):
#     pre_dragon_curve = dragon_curve[-1][:]
#     # print(pre_dragon_curve)
#     new_dragon_curve = [0] * len(pre_dragon_curve)
#     # print(next_dragon_curve)

#     for i in range(len(pre_dragon_curve)):
#         new_dragon_curve[i] = (pre_dragon_curve[-i-1]+1) % 4
#     # print(pre_dragon_curve, new_dragon_curve)
#     pre_dragon_curve.extend(new_dragon_curve)
#     dragon_curve.append(pre_dragon_curve)
# # for y in range(10):
# #     print(dragon_curve[y])

# for _ in range(N):
#     x, y, dd, g = map(int, input().split())
#     board[x][y] = 1

#     inc_xy = [[1, 0], [0, -1], [-1, 0], [0, 1]]
#     # print(x, y)
#     # print(dragon_curve[g])
#     for d in dragon_curve[g]:
#         d = (d + dd)%4
#         # print(d, end=' ')

#         nx, ny = x + inc_xy[d][0], y + inc_xy[d][1]
#         board[nx][ny] = 1

#         x, y = nx, ny
#     # print()

#     # for y in range(10):
#     #     for x in range(10):
#     #         print(board[x][y], end = ' ')
#     #     print()

# ans = 0
# for y in range(0, 100):
#     for x in range(0, 100):
#         if board[y][x] == 1 and board[y][x+1] == 1 and board[y+1][x] == 1 and board[y+1][x+1] == 1:
#             ans += 1
# print(ans)


# 15686 치킨 배달
# pm 05:05 ~ 05:40
# import sys
# input = sys.stdin.readline
# import itertools

# N, M = map(int, input().split())
# city = [list(map(int, input().split())) for _ in range(N)]

# home = []
# chicken = []
# for x in range(N):
#     for y in range(N):
#         if city[x][y] == 1:
#             home.append([x, y])
#         elif city[x][y] == 2:
#             chicken.append([x, y])
# # print(home, chicken)
# len_chicken = len(chicken)
# len_home = len(home)

# chicken_dist = [[0]*len_home for _ in range(len_chicken)]
# for c in range(len_chicken):
#     for h in range(len_home):
#         chicken_dist[c][h] = abs(chicken[c][0] - home[h][0]) + abs(chicken[c][1] - home[h][1])

# # for x in range(len_chicken):
#     # print(chicken_dist[x])

# chicken_idx = [i for i in range(len_chicken)]
# # print(chicken_idx)

# min_urban_chicken_dist = 1300
# for k in range(1, min(M, len_chicken)+1):
#     for cb in itertools.combinations(chicken_idx, k):
#         # print(*cb)
#         urban_chicken_dist = [100]*len_home
#         for x in cb:
#             for h in range(len_home):
#                 urban_chicken_dist[h] = min(urban_chicken_dist[h], chicken_dist[x][h])
#         # print(urban_chicken_dist)
#         if min_urban_chicken_dist > sum(urban_chicken_dist):
#             min_urban_chicken_dist = sum(urban_chicken_dist)

# print(min_urban_chicken_dist)


# 5373 큐빙
# pm 10:11 ~ 11:20 ~ .. 리스트부터 다시 짜야겠음

# 가장 윗면의 색상

# def copy_side(side):
#     # tmp_side = [[] for _ in range(3)]
#     # for x in range(3):
#     #     tmp_side[x] = side[x][:]

#     tmp_side = side[:]
#     return tmp_side

# for _ in range(int(input())):
#     n = int(input())
#     move = list(map(str, input().split()))
#     # print(move)

#     up = [['w']*3 for _ in range(3)]
#     down = [['y']*3 for _ in range(3)]
#     front = [['r']*3 for _ in range(3)]
#     back = [['o']*3 for _ in range(3)]
#     left = [['g']*3 for _ in range(3)]
#     right = [['b']*3 for _ in range(3)]

#     for m in move:
#         if m[0] == 'U':
#             # round
#             r = [back[0], right[0], front[0], left[0]]
#             if m[1] == '-':
#                 r = r[::-1]
                
#             tmp_last = copy_side(r[-1])
            
#             for idx in range(4):
#                 if idx != 3:
#                     for y in range(3):
#                         r[idx+1][y] = r[idx][y]
#                 else: # idx == 3:
#                     for y in range(3):
#                         r[0][y] = tmp_last[y]

#         elif m[0] == 'D':
#             # round
#             r = [back[2], left[2], front[2], right[2]]
#             if m[1] == '-':
#                 r = r[::-1]
                
#             tmp_last = copy_side(r[-1])
            
#             for idx in range(4):
#                 if idx != 3:
#                     for y in range(3):
#                         r[idx+1][y] = r[idx][y]
#                 else: # idx == 3:
#                     for y in range(3):
#                         r[0][y] = tmp_last[y]

#         # elif m[0] == 'F':
#             # r = [up[2], 'right', down[2][::-1], 'left']
#             # # for rr in r:
#             #     # print(type(rr))
#             # if m[1] == '-':
#             #     r = r[::-1]
            
#             # for idx in range(4):
#             #     if idx != 3:
#             #         if type(r[idx]) == list:
#             #             if r[idx+1] == 'left':
#             #                 for y in range(3):
#             #                     left[y][2] = r[idx][y]
#             #             else: # right
#             #         else: # string
#             #             if r[idx] == 'left':
#             #             else: # right

#             #     else: # idx == 3:
#             #         for y in range(3):

#         # elif m[0] == 'B':
#         # elif m[0] == 'L':
#         # else: # 'R'
        
#         # if m[1] == '-':
#         #     r == r[::-1]
    
        
#         # 해당 면 회전

#     print(up, down, front, back, left, right, sep = '\n')


# pm 10:58 ~ 11:50 clear

# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n = int(input())
#     rotation = list(map(str, input().rstrip().split()))
#     # print(n, rotation)

#     # 위 0, 아래 1, 앞 2, 뒤 3, 왼 4, 오 5
#     cube = [['w']*10, ['y']*10, ['r']*10, ['o']*10, ['g']*10, ['b']*10]
#     # print(cube)

#     for r in rotation:
#         if r[0] == 'U':
#             face = 0
#             target = [[[3, 3], [3, 2], [3, 1]], [[5, 3], [5, 2], [5, 1]],\
#                       [[2, 3], [2, 2], [2, 1]], [[4, 3], [4, 2], [4, 1]]]
#         elif r[0] == 'D':
#             face = 1
#             target = [[[3, 9], [3, 8], [3, 7]], [[4, 9], [4, 8], [4, 7]],\
#                       [[2, 9], [2, 8], [2, 7]], [[5, 9], [5, 8], [5, 7]]] 
#         elif r[0] == 'F':
#             face = 2
#             target = [[[0, 7], [0, 8], [0, 9]], [[5, 1], [5, 4], [5, 7]],\
#                       [[1, 7], [1, 8], [1, 9]], [[4, 9], [4, 6], [4, 3]]] 
#         elif r[0] == 'B':
#             face = 3
#             target = [[[0, 3], [0, 2], [0, 1]], [[4, 1], [4, 4], [4, 7]],\
#                       [[1, 3], [1, 2], [1, 1]], [[5, 9], [5, 6], [5, 3]]] 
#         elif r[0] == 'L':
#             face = 4
#             target = [[[0, 1], [0, 4], [0, 7]], [[2, 1], [2, 4], [2, 7]],\
#                       [[1, 9], [1, 6], [1, 3]], [[3, 9], [3, 6], [3, 3]]]
#         else: # r[0] == 'R':
#             face = 5
#             target = [[[0, 9], [0, 6], [0, 3]], [[3, 1], [3, 4], [3, 7]],\
#                       [[1, 1], [1, 4], [1, 7]], [[2, 9], [2, 6], [2, 3]]]
        
#         if r[1] == '-':
#             target = target[::-1]
        
#         tmp_backup = [0]*3
#         for y in range(3):
#             tmp_backup[y] = cube[target[0][y][0]][target[0][y][1]]
#         # print(tmp_backup)

#         # 4 -> len(target)
#         for i in range(3, -1, -1):
#             for y in range(3):
#                 if i != 0:
#                     cube[target[(i+1)%4][y][0]][target[(i+1)%4][y][1]] = cube[target[i][y][0]][target[i][y][1]]
#                 else:
#                     cube[target[(i+1)%4][y][0]][target[(i+1)%4][y][1]] = tmp_backup[y]

#         target = [[1, 3, 9, 7], [2, 6, 8, 4]]
#         for t in target:
#             if r[1] == '-':
#                 t = t[::-1]
#             t_backup = cube[face][t[0]]
            
#             for i in range(3, -1, -1):
#                 if i != 0:
#                     cube[face][t[(i+1)%4]] = cube[face][t[i]]
#                 else:
#                     cube[face][t[(i+1)%4]] = t_backup

#     for x in range(3):
#         print(*cube[0][1+(x*3):4+(x*3)], sep='')


# 16234 인구 이동
# am 12:02 ~ 12:37
# 시간 제출 -> PyPy3 제출하니 통과
# import sys
# input = sys.stdin.readline
# from collections import deque

# def check_need_popluation_move(N, L, R, board, inc_xy):
#     for x in range(N):
#         for y in range(N):
#             for p_x, p_y in inc_xy:
#                 nx, ny = x + p_x, y + p_y
#                 if 0 <= nx < N and 0 <= ny < N :
#                     if L <= abs(board[x][y] - board[nx][ny]) <= R:
#                         return True
#     return False

# N, L, R = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# need_population_move = check_need_popluation_move(N, L, R, board, inc_xy)

# ans = 0
# while need_population_move:
#     ans += 1
    
#     que = deque()
#     check = [[0]*N for _ in range(N)]

#     # 시작점 찾기
#     for x in range(N):
#         for y in range(N):
#             for p_x, p_y in inc_xy:
#                 nx, ny = x + p_x, y + p_y
#                 if 0 <= nx < N and 0 <= ny < N :
#                     if L <= abs(board[x][y] - board[nx][ny]) <= R:
#                         if check[x][y] == 0:
#                             check[x][y] = 1
#                             que.append([x, y])

#     # 시작점을 기준으로 bfs 전개해서 인구이동 구현
#     check = [[0]*N for _ in range(N)]
#     # que : 기준점 xy que
#     while que:
#         x, y = que.popleft()
#         if check[x][y] == 0:
#             check[x][y] = 1
#             population = board[x][y]
#             area = 1
            
#             # 방문한 xy를 저장하기 위한 set
#             xy_set = set({tuple([x, y])})
#             # print(xy_set)

#             # pop_que -> 인구수, 칸 개수 구하기 위한 큐
#             pop_que = deque([[x, y]])
#             while pop_que:
#                 kx, ky = pop_que.popleft()
#                 # print("kx, ky", kx, ky)
#                 for p_x, p_y in inc_xy:
#                     nx, ny = kx + p_x, ky + p_y
#                     if 0 <= nx < N and 0 <= ny < N :
#                         if L <= abs(board[kx][ky] - board[nx][ny]) <= R:
#                             if check[nx][ny] == 0:
#                                 check[nx][ny] = 1

#                                 pop_que.append([nx, ny])
#                                 xy_set.add(tuple([nx, ny]))
#                                 population += board[nx][ny]
#                                 area += 1

#             new_pop = population//area
#             for sx, sy in xy_set:
#                 board[sx][sy] = new_pop

#     # for x in range(N):
#     #     print(board[x])
#     # print()
#     # input()
#     need_population_move = check_need_popluation_move(N, L, R, board, inc_xy)

# print(ans)


# 16235 나무 재테크
# am 12:42 ~ 01:40 (시간초과) ~ 02:06

# import sys
# input = sys.stdin.readline
# # from queue import PriorityQueue
# # from collections import defaultdict
# from collections import deque

# N, M, K = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(N)]
# water = [[5]*N for _ in range(N)]
# # 우선순위 큐(어린 나무부터), tree_to_water(여름)
# # tree = [[PriorityQueue() for _ in range(N)] for _ in range(N)]
# tree = [[deque() for _ in range(N)] for _ in range(N)]
# inc_xy = [[p_x, p_y] for p_x in [-1, 0, 1] for p_y in [-1, 0, 1] if not (p_x == 0 and p_y == 0)]

# for _ in range(M):
#     x, y, z = map(int, input().split())
#     # tree[x-1][y-1].put(z)
#     tree[x-1][y-1].append(z)
# for x in range(N):
#     for y in range(N):
#         tree[x][y] = deque(sorted(tree[x][y]))
#         # print(tree[x-1][y-1].queue, end = ' ')
# #     print()

# # K년 후
# for _ in range(K):
#     # breeding_dict = defaultdict(int)
#     breeding_dict = dict()

#     # 봄, 여름까지
#     for x in range(N):
#         for y in range(N):
#             # que = PriorityQueue()
#             que = deque()
#             tree_to_water = 0

#             # if tree[x][y]:
#             #     tree[x][y] = deque(sorted(tree[x][y]))

#             while tree[x][y]:
#                 # print("haha")
#                 tree_age = tree[x][y].popleft()
#                 if water[x][y] >= tree_age:
#                     water[x][y] -= tree_age
#                     # 1살 추가
#                     tree_age += 1
#                     # 가을용
#                     if tree_age % 5 == 0:
#                         tuple_xy = tuple([x, y])
#                         if tuple_xy not in breeding_dict:
#                             breeding_dict[tuple_xy] = 1
#                         else:
#                             breeding_dict[tuple_xy] += 1
#                     que.append(tree_age)
#                 else:
#                     tree_to_water += tree_age//2

#             tree[x][y] = que
#             # print(x, y, que.queue, end = ' ')
#             water[x][y] += tree_to_water
#     #     print()
#     # print()

#     # 가을
#     for x, y in breeding_dict:
#         # print(x, y)
#         for p_x, p_y in inc_xy:
#             nx, ny = x + p_x, y + p_y
#             if 0 <= nx < N and 0 <= ny < N:
#                 # print("num", breeding_dict[tuple([x, y])])
#                 for _ in range(breeding_dict[tuple([x, y])]):
#                 #     tree[nx][ny].put(1)
#                     tree[nx][ny].appendleft(1)
#                 # tree[nx][ny].extend([1 for _ in range(breeding_dict[tuple([x, y])])])

#     # 겨울
#     for x in range(N):
#         for y in range(N):
#             water[x][y] += A[x][y]

# ans = 0
# for x in range(N):
#     for y in range(N):
#         # print(tree[x][y].qsize(), end = ' ')
#         ans += len(tree[x][y])
#     # print()
# print(ans)


# 17144 미세먼지 안녕!
# pm 04:05 ~ 04:44
# Python3 시간초과 → PyPy3 통과
# import sys
# input = sys.stdin.readline

# R, C, T = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(R)]
# inc_xy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# # T초가 지난 후 구사과 방에 남아있는 미세먼지의 양을 출력
# for _ in range(T):
#     tmp_A = [[0]*C for _ in range(R)]

#     # 확산 기준점 잡기
#     fine_dust = set()
#     air_filter = set()
#     for x in range(R):
#         for y in range(C):
#             if A[x][y] > 0:
#             # if A[x][y] >= 5:
#                 fine_dust.add(tuple([x, y]))
#             elif A[x][y] == -1:
#                 air_filter.add(tuple([x, y]))
#     # print(fine_dust)

#     # 확산 구현 tmp_A에 따로 저장
#     for x, y in fine_dust:
#         cnt = 0
#         for p_x, p_y in inc_xy:
#             nx, ny = x + p_x, y + p_y
#             if 0 <= nx < R and 0 <= ny < C and A[nx][ny] != -1:
#                 tmp_A[nx][ny] += A[x][y]//5
#                 cnt += 1
#         tmp_A[x][y] -= (A[x][y]//5)*cnt
    
#     # 미세먼지 확산 일괄 적용
#     for x in range(R):
#         for y in range(C):
#             A[x][y] += tmp_A[x][y]
    
#     # 공기청정기 작동
#     cnt = 0
#     for x, y in air_filter:
#         # 윗칸 공기청정기
#         if cnt == 0:
#             # ↓
#             for kx in range(x-1, -1, -1):
#                 A[kx+1][y] = A[kx][y]

#             # ←
#             for ky in range(C-1):
#                 A[0][ky] = A[0][ky+1]

#             # ↑
#             for kx in range(x):
#                 A[kx][C-1] = A[kx+1][C-1]

#             # →
#             for ky in range(C-2, -1, -1):
#                 A[x][ky+1] = A[x][ky]

#             A[x][y] = -1
#             A[x][y+1] = 0
            
#         else:
#             # ↑
#             for kx in range(x, R-1):
#                 A[kx][y] = A[kx+1][y]

#             # ←
#             for ky in range(C-1):
#                 A[R-1][ky] = A[R-1][ky+1]

#             # ↓
#             for kx in range(R-1, x, -1):
#                 A[kx][C-1] = A[kx-1][C-1]

#             # →
#             for ky in range(C-2, -1, -1):
#                 A[x][ky+1] = A[x][ky]

#             A[x][y] = -1
#             A[x][y+1] = 0

#         cnt += 1

# ans = 0
# for x in range(R):
#     for y in range(C):
#         if A[x][y] > 0:
#             ans += A[x][y]
# print(ans)


# 17143 낚시왕
# pm 10:00 ~ 11:15
# 1번째 제출에 clear ㅎㅎ

# import sys
# input = sys.stdin.readline

# R, C, M = map(int, input().split())
# board = [[0]*C for _ in range(R)]

# # shark = [[[0, 0, 0] for _ in range(C)] for _ in range(R)]
# shark = dict()

# dd = [[], [-1, 0], [1, 0], [0, 1], [0, -1]]
# for _ in range(M):
#     r, c, s, d, z = map(int, input().split())
#     # shark[r-1][c-1] = [s, d, z]
#     if d in [1, 2]:
#         shark[tuple([r-1, c-1])] = [s%(2*(R-1)), d, z]
#     else:
#         shark[tuple([r-1, c-1])] = [s%(2*(C-1)), d, z]
# # print(shark)

# # for x in range(R):
# #     print(shark[x])
# # print()

# fishman_y = -1
# ans = 0
# for _ in range(C):
#     # 1칸 이동해서 가장 가까운 상어 한 마리 낚시
#     fishman_y += 1
#     for x in range(R):
#         target = tuple([x, fishman_y])
#         # print("target", target)
#         if target in shark:
#             # print("get", target, shark[target])
#             ans += shark[target][2]
#             del(shark[target])
#             break
#     # print(shark)

#     # 상어 이동
#     new_shark = dict()
#     for x, y in shark:
#         # print(x, y)
#         s, d, z = shark[tuple([x, y])]
        
#         # 새로운 x, y 계산
#         left_s = s
#         nx, ny = x, y

#         while left_s > 0:
#             if d == 1:
#                 move = min(left_s, nx)
#                 left_s -= move
#                 nx -= move
                
#                 if left_s > 0:
#                     d = 2

#             elif d == 2:
#                 move = min(left_s, (R-1)-nx)
#                 left_s -= move
#                 nx += move
                
#                 if left_s > 0:
#                     d = 1

#             elif d == 3:
#                 move = min(left_s, (C-1)-ny)
#                 left_s -= move
#                 ny += move

#                 if left_s > 0:
#                     d = 4
#             else:
#                 move = min(left_s, ny)
#                 left_s -= move
#                 ny -= move

#                 if left_s > 0:
#                     d = 3

#         target = tuple([nx, ny])
#         # new_shark에 있는 경우 → 비교
#         if target in new_shark:
#             if new_shark[target][2] < z:
#                 new_shark[target] = [s, d, z]
#         # 없으면 그냥 추가
#         else:
#             new_shark[target] = [s, d, z]

#     shark = new_shark
#     # print("new_shark")
#     # print(new_shark)
#     # print()

# print(ans)