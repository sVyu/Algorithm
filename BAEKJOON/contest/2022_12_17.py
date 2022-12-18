# 2022 서울사이버대학교 프로그래밍 경진대회 (SCUPC)
# A번 - 빅데이터? 정보보호!
# from collections import defaultdict

# N = int(input())
# s = list(input())
# len_s = len(s)

# idx = 0
# interest = defaultdict(int)

# while idx < len_s:
#     if s[idx] == 's':
#         interest['security'] += 1
#         idx += 8
#     else:
#         interest['bigdata'] += 1
#         idx += 7

# if interest['security'] > interest['bigdata']: print("security!")
# elif interest['security'] < interest['bigdata']: print("bigdata?")
# else: print("bigdata? security!")


# B번 - 멘토와 멘티
# import sys
# input = sys.stdin.readline

# N = int(input())
# # mentor - mentee
# mm = [list(input().rstrip().split()) for _ in range(N)]
# # print(mm)

# mm = sorted(mm, key=lambda x:(x[0], x[1]), reverse= True)
# print(mm)


# from collections import defaultdict
# import sys
# input = sys.stdin.readline

# mm = defaultdict(list)
# for _ in range(int(input())):
#     key, val = map(str, input().rstrip().split())
#     mm[key].append(val)
# mm = sorted(mm.items(), key=lambda x:(x[0], x[1]))
# # print(mm) # type : list

# for mentor, mentee in mm:
#     mentee = sorted(mentee, reverse=True)
#     for each_mentee in mentee:
#         print(mentor, each_mentee)


# C번

#
# basic_s = list(input())
# target_s = list(input())

# total_len = 1
# len_basic_s = len(basic_s)
# while total_len <= len_basic_s:
#     ans_s = ['A'] * total_len
#     for idx in range(total_len):
#         ans_s[idx] = chr(((ord(target_s[idx]) - ord(basic_s[idx]))%26-1)%26 + 65)

#     len_ans_s = len(ans_s)
#     pos_check = True
#     for iidx in range(idx+1, len_basic_s):
#         if (ord(ans_s[iidx % len_ans_s])-65+1)%26 != (ord(target_s[iidx]) - ord(basic_s[iidx]))%26:
#             pos_check = False
#         # if ans_s == ["S","E","O","U","L"]:
#         #     print(ord(ans_s[iidx % len_ans_s])-65+1, (ord(target_s[iidx]) - ord(basic_s[iidx]))%26)
#         break
    
#     if pos_check:
#         print(*ans_s, sep = '')
#         break

#     total_len += 1

# import sys
# input = sys.stdin.readline
# basic_s = list(input().rstrip())
# target_s = list(input().rstrip())

# total_len = 1
# len_basic_s = len(basic_s)
# while total_len <= len_basic_s:
#     ans_s = [0] * total_len
#     for idx in range(total_len):
#         ans_s[idx] = (ord(target_s[idx]) - ord(basic_s[idx]))%26

#     len_ans_s = len(ans_s)
#     pos_check = True
#     for iidx in range(idx+1, len_basic_s):
#         if target_s[iidx] != chr((ord(basic_s[iidx])-65 + ans_s[iidx % len_ans_s])%26+65):
#             pos_check = False
#             break
    
#     if pos_check:
#         # print(idx, iidx)
#         # print(ans_s)
#         for a in ans_s:
#             if a == 0: print("Z", end = '')
#             else: print(chr(a+64), end = '')
#         break

#     total_len += 1


# try 2
# basic_s = list(input().rstrip())
# target_s = list(input().rstrip())

# len_basic_s = len(basic_s)
# gap_s = [0]*len_basic_s

# for idx in range(len_basic_s):
#     gap_s[idx] = (ord(target_s[idx]) - ord(basic_s[idx]))%26
# # print(gap_s)

# total_len = 1
# while True:
#     pos = True
#     for iidx in range(total_len, len_basic_s):
#         if gap_s[iidx % total_len] != gap_s[iidx]:
#             pos = False
#             break
    
#     if pos:
#         break

#     total_len += 1
# # print(gap_s, total_len)

# for g in gap_s[:total_len]:
#     if g == 0:
#         print("Z", end='')
#     else:
#         print(chr(g+64), end='')


# try 3
# 에라토스테네스의 체 (sieve of Eratosthenes)
# def sieve(num_limit):
#     num = [False] + [True]*num_limit
#     for i in range(2, num_limit+1):
#         if num[i]:
#             for idx in range(i*2, num_limit+1, i):
#                 num[idx] = False

#     return [i for i in range(len(num)) if num[i]]

# def solve():
#     basic_s = list(input().rstrip())
#     target_s = list(input().rstrip())

#     len_basic_s = len(basic_s)
#     gap_s = [0]*len_basic_s

#     # 차이 계산
#     for idx in range(len_basic_s):
#         gap_s[idx] = (ord(target_s[idx]) - ord(basic_s[idx]))%26
#     # print(gap_s)

#     # 1과 소수 숫자에 해당하는 길이에 대해서 암호 해독 가능한지 검사
#     for ans_len in sieve(len_basic_s):
#         pos = True
#         for iidx in range(ans_len, len_basic_s):
#             if gap_s[iidx % ans_len] != gap_s[iidx]:
#                 pos = False
#                 break
        
#         if pos:
#             break

#     # 정답 반환 (len_basic_s 최대 길이 이하)
#     for g in gap_s[:ans_len]:
#         if g == 0:
#             print("Z", end='')
#         else:
#             print(chr(g+64), end='')

# solve()