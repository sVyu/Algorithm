import sys
input = sys.stdin.readline

ans = 0
ws = set()
for _ in range(int(input())):
    word = input().rstrip()
    if word == 'ENTER':
        ans += len(ws)
        ws = set()
    else:
        ws.add(word)

ans += len(ws)
print(ans)