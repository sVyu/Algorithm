import sys
input = sys.stdin.readline

'''
ZERO        Z
TWO         W
FOUR        U
SIX         X
EIGHT       G
'''
'''
ONE         O
THREE       T
FIVE        F
SEVEN       S
NINE        I
'''

def delete_with_base_alphabet(cnts:list, base_alphabet:str, idx:int, target_values:list, target_chars:list, ans:list):
    ti = ord(base_alphabet)-65
    cnt = cnts[ti]
    if(cnt):
        for _ in range(cnt):
            ans.append(target_values[idx])
        for c in target_chars[idx]:
            cnts[ord(c)-65] -= cnt

def solve():
    t = int(input())
    for case_num in range(1, t+1):
        s = input().rstrip()

        ans = []
        cnts = [0]*26
        for c in s:
            cnts[ord(c)-65] += 1
        # print(cnts)

        target_values = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
        target_chars = ["ZERO", "TWO", "FOUR", "SIX", "EIGHT", "ONE", "THREE", 'FIVE', 'SEVEN', 'NINE']
        bases = "ZWUXGOTFSI"
        for idx in range(10):
            delete_with_base_alphabet(cnts, bases[idx], idx, target_values, target_chars, ans)
        # print(ans)

        ans.sort()
        # print(ans)

        print(f'Case #{case_num}: {"".join(map(str, ans))}')

solve()