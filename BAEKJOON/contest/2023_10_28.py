# 2023 제1회 춘배컵

# A번 감마선을 맞은 컴퓨터
# def solve():
#     for x in range(15):
#         ss = list(input().split())
#         for s in ss:
#             if s == 'w':
#                 print('chunbae')
#                 return
#             if s == 'b':
#                 print('nabi')
#                 return
#             if s == 'g':
#                 print('yeongcheol')
#                 return

# solve()


# B 무지개 만들기
# N = int(input())
# ss = input()

# small_pos, big_pos = True, True
# for s in 'roygbiv':
#     if s not in ss:
#         small_pos = False
#         break

# for s in 'ROYGBIV':
#     if s not in ss:
#         big_pos = False
#         break

# if small_pos and big_pos:
#     print('YeS')
# elif small_pos:
#     print('yes')
# elif big_pos:
#     print("YES")
# else:
#     print('NO!')


# 4836 춤
# import sys
# lines = sys.stdin.readlines()

# def check_rule1(ss, i, len_ss):
#     if not (((i >= 1) and ss[i-1] == 'jiggle') or\
#             ((i >= 2) and ss[i-2] == 'jiggle')):
#             if (i < len_ss-1):
#                 if (ss[i+1] != 'twirl'):
#                     return False
#             else:
#                 return False
#     return True

# for ss in lines:
#     keep_rules = [True]*6
#     # print(ss.rstrip())

#     ss = ss.rstrip().split()
#     len_ss = len(ss)
#     # print('ss :', ss)

#     # 1번
#     for i in range(len_ss):
#         if ss[i] == 'dip':
#             keep_rule_1 = check_rule1(ss, i, len_ss)
#             if not keep_rule_1:
#                 keep_rules[1] = False
#                 break

#     # 2번
#     if (len_ss < 3) or (ss[-3:] != ['clap', 'stomp', 'clap']):
#         keep_rules[2] = False

#     # 3번
#     if ('twirl' in ss) and ('hop' not in ss):
#         keep_rules[3] = False

#     # 4번
#     if ss[0] == 'jiggle':
#         keep_rules[4] = False

#     # 5번
#     if 'dip' not in ss:
#         keep_rules[5] = False

#     idx_break_rules = [i for i in range(1, 6) if not keep_rules[i]]
#     # print("idxs_", idx_break_rules)

#     if not idx_break_rules:
#         print(f'form ok: ', end='')
#         print(*ss, end='')
#     else:
#         if len(idx_break_rules) == 1:
#             print(f'form error {idx_break_rules[0]}: ', end='')
#         else:
#             print(f'form errors ', end='')
#             print(*idx_break_rules[:-1], sep=', ', end=' ')
#             print(f'and {idx_break_rules[-1]}: ', end='')

#         for i in range(len_ss):
#             if ss[i] == 'dip':
#                 if not check_rule1(ss, i, len_ss):
#                     print('DIP ', end='')
#                 else:
#                     print('dip ', end='')
#             else:
#                 print(f'{ss[i]} ', end='')
#     print()


# Ping! 9479
# def t(n):
#     if n: return 0
#     else: return 1

# def solve():
#     ss = input()
#     while ss != '0':
#         ss = list(map(int, ss))
#         len_ss = len(ss)
#         target = [0]*(len_ss)
#         ans = []

#         for i in range(1, len_ss):
#             if ss[i] != target[i]:
#                 for j in range(i, len_ss, i):
#                     target[j] = t(target[j])
#                 ans.append(i)
#         # print(target)
#         print(*ans)

#         ss = input()

# solve()


# 28086 미소녀 컴퓨터 파루빗토 쨩
# print(14/-3)

# # dec to oct
# def d_to_o(n):
#     n = int(n)
#     sign = 1 if n > 0 else -1
#     n = abs(n)
#     s = ''
#     while n > 0:
#         s += str(n % 8)
#         n //= 8
#     return sign*int(''.join(s[::-1]) if s else 0)

# # oct to dec
# def o_to_d(n):
#     n = int(n)
#     sign = 1 if n > 0 else -1
#     n = abs(n)
#     k, m = 0, 1
#     while n > 0:
#         k += (n % 10)*m
#         n //= 10
#         m *= 8
#     return sign*int(k)

# def solve():
#     exp = input()
#     ans = -1

#     if '*' in exp:
#         a, b = map(o_to_d, exp.split('*'))
#         ans = d_to_o(a*b)
#     elif '/' in exp:
#         a, b = map(o_to_d, exp.split('/'))
#         if b == 0:  ans = 'invalid'
#         else:       ans = d_to_o(a//b)
#     elif '+' in exp[1:]:
#         a, b = map(o_to_d, exp.split('+')[-2:])
#         ans = d_to_o(a+b)
#     else:
#         new_ab = [-1, -1]
#         for i in range(len(exp)-1, -1, -1):
#             if exp[i] == '-':
#                 new_ab = [exp[:i], exp[i+1:]]
#                 # print(new_ab)
#                 break
#         a, b = map(o_to_d, new_ab)
#         ans = d_to_o(a-b)

#     print(ans)

# solve()


# 27496 발머의 피크 이론
# N, L = map(int, input().split())
# ns = list(map(int, input().split()))

# ans, now = 0, 0
# for i in range(N):
#     now += ns[i]
#     if i >= L:
#         now -= ns[i-L]

#     if 129 <= now <= 138:
#         ans += 1

# print(ans)


# 9272 상근이의 아이디어
# n1, n2 = map(int, input().split())
# print((n2-n1)*(n2-n1+1)//2)


# 19941 햄버거 분배
# N, K = map(int, input().split())
# ss = list(input())

# eaten = [False]*N
# ans = 0

# for i in range(N):
#     if ss[i] == 'P':
#         for j in range(max(0, i-K), min(N, i+K+1)):
#             if ss[j] == 'H' and not eaten[j]:
#                 eaten[j] = True
#                 ans += 1
#                 break

# print(ans)


