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
