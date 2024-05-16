import sys
input = sys.stdin.readline

for _ in range(int(input())):
    print('odd' if int(input())%2 else 'even')