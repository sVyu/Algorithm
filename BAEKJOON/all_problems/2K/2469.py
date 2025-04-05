import sys
input = sys.stdin.readline

def move_by_ladder(k, s, ladder):
    for i in range(k-1):
        c = ladder[i]
        if(c == '-'):
            s[i], s[i+1] = s[i+1], s[i]
    return s

def solve():
    k = int(input())
    n = int(input())
    target_s = list(input().rstrip())
    # print(target_s)

    base_s = [chr(65+i) for i in range(k)]
    # print("base_s", base_s)

    ladders = [input().rstrip() for _ in range(n)]
    question_mark_index = 0
    for i in range(n):
        if(ladders[i][0] == '?'):
            question_mark_index = i
    # print(question_mark_index)

    for i in range(question_mark_index):
        ladder = ladders[i]
        base_s = move_by_ladder(k, base_s, ladder)
    # print(base_s)

    for i in range(question_mark_index+1, n):
        ladder = ladders[n-1+question_mark_index+1-i]
        target_s = move_by_ladder(k, target_s, ladder)
    # print("target_s", target_s)

    ans = ['_' for _ in range(k-1)]
    # print("ans", ans)

    i = 0
    while(i < (k-1)):
        if(base_s[i] == target_s[i]):
            ans[i] = '*'
            i += 1
        elif(base_s[i] == target_s[i+1] and\
            base_s[i+1] == target_s[i]):
            if(ans[i] != '-'):
                ans[i] = '-'
                if(i+1 < (k-1)):
                    ans[i+1] = '*'
                i += 2
            else:
                for j in range(k-1):
                    ans[j] = 'x'
                break
        else:
            for j in range(k-1):
                ans[j] = 'x'
            break
    print(''.join(ans))

solve()