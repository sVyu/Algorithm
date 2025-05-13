import sys
input = sys.stdin.readline

def solve():
    s = input().rstrip()
    # print(s)

    cnts = [0]*26
    for c in s:
        cnts[ord(c)-65] += 1
    # print(cnts)

    odd_num_idx = -1
    for i in range(26):
        if(cnts[i]%2):
            if(odd_num_idx != -1):
                print("I'm Sorry Hansoo")
                return
            odd_num_idx = i

    # print logic
    for i in range(26):
        if(cnts[i]//2):
            print(chr(65+i)*(cnts[i]//2), end='')

    if(odd_num_idx != -1):
        print(chr(65+odd_num_idx), end='')

    for i in range(25, -1, -1):
        if(cnts[i]//2):
            print(chr(65+i)*(cnts[i]//2), end='')

solve()