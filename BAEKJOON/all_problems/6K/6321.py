import sys
input = sys.stdin.readline

for n in range(1, int(input())+1):
    print(f'String #{n}')
    ss = list(input().rstrip())
    for c in ss:
        print(chr(((ord(c)-65+1)%26)+65), end='')
    print()
    print()