# 1. 7게임
# for _ in range(5):
#     k = list(map(int, input()))
#     # print(k)
    
#     a = 0
#     for idx in range(0, 7, 2):
#         # print(k[idx])
#         a += k[idx]
#     for idx in range(1, 7, 2):
#         if k[idx] != 0:
#             a *= k[idx]
#     print(a % 10)


# 2. 제곱암호
# N = int(input())
# S = list(map(str, input()))

# for idx in range(0, N, 2):
#     alphabet_val = ord(S[idx]) - 97
#     alphabet_val += int(S[idx+1])**2
#     alphabet_val %= 26
#     print(chr(alphabet_val+97), end='')

# 3. 비밀 편지
# E : Encode, E : Decode
# for _ in range(int(input())):
#     before_sentence = list(input())
#     token = list(map(str, input().split()))
#     # print(before_sentence, token)
#     len_token = len(token[1])
#     if token[0] == 'E':
#         toggle = 1
#     else:
#         toggle = -1

#     for idx in range(len(before_sentence)):
#         ord_before_sentence_idx = ord(before_sentence[idx])
#         if 65 <= ord_before_sentence_idx <= 90 or\
#             97 <= ord_before_sentence_idx <= 122:
#             minus_val = 0
#             if 65 <= ord_before_sentence_idx <= 90:
#                 minus_val = 65
#             else:
#                 minus_val = 97

#             alphabet_idx = ord(before_sentence[idx]) - minus_val
#             # shift_val 
#             shift_val = ord(token[1][idx % len_token]) % 26
#             alphabet_idx = (alphabet_idx + 26 + (toggle * shift_val)) % 26
#             print(chr(alphabet_idx + minus_val), end='')
#         else:
#             print(before_sentence[idx], end='')
#     print()


# 4. 경쟁 배타의 원리
# import sys
# input = sys.stdin.readline

# board = [[0] * 1000 for _ in range(1000)]
# N, K = map(int, input().split())
# for _ in range(N):
#     x1, y1, x2, y2 = map(int, input().split())
#     for x in range(x1+1, x2+1):
#         for y in range(y1+1, y2+1):
#             board[x][y] += 1

# ans = 0
# for x in range(1000):
#     for y in range(1000):
#         if board[x][y] == K:
#             ans += 1
# print(ans)


# 1
# for _ in range(5):
#     K = list(map(int, input()))
#     a = 0
#     for i in range(0, 7, 2):
#         a += K[i]
#     for i in range(1, 7, 2):
#         if K[i] != 0:
#             a *= K[i]
#     print(a % 10)

# 2
# N = int(input())
# S = list(input())

# for i in range(0, N, 2):
#     print(chr((((ord(S[i])-97) + int(S[i+1])**2)%26)+97), end = '')


# 3
# import sys
# import string

# input = sys.stdin.readline

# alpha_sm = list(string.ascii_lowercase)
# alpha_bi = list(string.ascii_uppercase)

# for i in range(int(input())):
#     S = list(input().rstrip())
#     cmd, key = map(str, input().split())

#     ans = ''
#     idx = 0
#     if cmd == 'E':
#         for i in S:
#             if i in alpha_sm:
#                 ans += alpha_sm[(alpha_sm.index(i) + (ord(key[idx]))) %26]
#             elif i in alpha_bi:
#                 ans += alpha_bi[(alpha_bi.index(i) + (ord(key[idx]))) %26]
#             else:
#                 ans += i

#             idx += 1
#             if idx == len(key):
#                 idx = 0

#     else: # cmd == 'D':
#         for i in S:
#             if i in alpha_sm:
#                 ans += alpha_sm[(alpha_sm.index(i) - (ord(key[idx]))) %26]
#             elif i in alpha_bi:
#                 ans += alpha_bi[(alpha_bi.index(i) - (ord(key[idx]))) %26]
#                 val = (alpha_bi.index(i) - (ord(key[idx])))
#                 # print(val, val % 26)
#                 # 음수여도 %값은 0이상이구나
#             else:
#                 ans += i

#             idx += 1
#             if idx == len(key):
#                 idx = 0
        
#     print(ans)

# import sys
# import string

# input = sys.stdin.readline

# alpha_sm = list(string.ascii_lowercase)
# alpha_bi = list(string.ascii_uppercase)

# for i in range(int(input())):
#     S = list(input().rstrip())
#     cmd, key = map(str, input().split())

#     ans = ''
#     idx = 0
#     for i in S:
#         if i in alpha_sm:
#             if cmd == 'E':
#                 ans += alpha_sm[(alpha_sm.index(i) + (ord(key[idx]))) %26]
#             else:
#                 ans += alpha_sm[(alpha_sm.index(i) - (ord(key[idx]))) %26]

#         elif i in alpha_bi:
#             if cmd == 'E':
#                 ans += alpha_bi[(alpha_bi.index(i) + (ord(key[idx]))) %26]
#             else:
                
#                 ans += alpha_bi[(alpha_bi.index(i) - (ord(key[idx]))) %26]
#         else:
#             ans += i

#         idx += 1
#         if idx == len(key):
#             idx = 0
        
#     print(ans)


# 4 경쟁 배타의 원리
# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
# board = [[0]*1002 for _ in range(1002)] # 0 ~ 1001
# for _ in range(N):
#     x1, y1, x2, y2 = map(int, input().split())
#     # board[x1][y1] = 1
#     board[x1][y1] += 1
#     board[x1][y2] += -1
#     board[x2][y1] += -1
#     board[x2][y2] += 1

# for x in range(1002):
#     for y in range(1, 1002):
#         board[x][y] += board[x][y-1]

# for y in range(1002):
#     for x in range(1, 1002):
#         board[x][y] += board[x-1][y]

# ans = 0
# for x in range(1002):
#     for y in range(1002):
#         if board[x][y] == K:
#             ans += 1
# print(ans)