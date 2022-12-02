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
