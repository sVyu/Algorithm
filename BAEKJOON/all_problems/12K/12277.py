import sys
input = sys.stdin.readline

def n_to_str(n):
    if n == 0:      return 'zero'
    elif n == 1:      return 'one'
    elif n == 2:    return 'two'
    elif n == 3:    return 'three'
    elif n == 4:    return 'four'
    elif n == 5:    return 'five'
    elif n == 6:    return 'six'
    elif n == 7:    return 'seven'
    elif n == 8:    return 'eight'
    elif n == 9:    return 'nine'

def cnt_naming(n, cnt):
    nstr = n_to_str(n)

    if cnt == 1:    return nstr
    elif cnt == 2:  return f'double {nstr}'
    elif cnt == 3:  return f'triple {nstr}'
    elif cnt == 4:  return f'quadruple {nstr}'
    elif cnt == 5:  return f'quintuple {nstr}'
    elif cnt == 6:  return f'sextuple {nstr}'
    elif cnt == 7:  return f'septuple {nstr}'
    elif cnt == 8:  return f'octuple {nstr}'
    elif cnt == 9:  return f'nonuple {nstr}'
    elif cnt == 10: return f'decuple {nstr}'
    else: return ' '.join([nstr]*cnt)

def solve():
    for case in range(int(input())):
        ns, split_cnts = input().split()
        split_cnts = map(int, split_cnts.split('-'))

        # seperate phone number
        new_ns = []
        l, r = 0, 0
        for split_cnt in split_cnts:
            r = l+split_cnt
            new_ns.append(ns[l:r])
            l = r
        # print(new_ns)

        # print logic
        print(f'Case #{case+1}: ', end='')
        for new_n in new_ns:
            pre = ''
            cnt = 0
            for c in new_n:
                if pre == c:
                    cnt += 1
                else:
                    if pre:
                        print(cnt_naming(int(pre), cnt), end=' ')
                    cnt = 1
                pre = c
            print(cnt_naming(int(pre), cnt), end=' ')
        print()

solve()