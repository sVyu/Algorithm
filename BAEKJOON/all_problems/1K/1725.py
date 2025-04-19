import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    zs = [int(input()) for _ in range(n)]

    ans = 0
    stack = []
    for i in range(n):
        while(stack and zs[stack[-1]] > zs[i]): #zs[stack[-1]]
            h = zs[stack.pop()]
            w = (i-1-stack[-1]) if stack else i
            ans = max(ans, w*h)
        stack.append(i)

    while(stack):
        h = zs[stack.pop()]
        w = (n-1-stack[-1]) if stack else n
        ans = max(ans, w*h)

    print(ans)

solve()