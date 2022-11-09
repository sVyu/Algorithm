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
#             alphabet_idx = (alphabet_idx + 26 + (toggle *shift_val)) % 26
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