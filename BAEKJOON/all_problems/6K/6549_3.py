# Âü°í : https://www.acmicpc.net/blog/view/12
def solve():
    ns = list(map(int, input().split()))
    while ns[0] != 0:
        n, zs = ns[0], ns[1:]
        # print(n, zs)

        stack = []
        ans = 0
        for i in range(n):
            while(stack and zs[stack[-1]] > zs[i]):
                h = zs[stack.pop()]
                w = (i-1-stack[-1]) if stack else i #
                ans = max(ans, w*h)
            stack.append(i)

        while(stack):
            h = zs[stack.pop()]
            w = (n-1-stack[-1]) if stack else n #
            ans = max(ans, w*h)

        print(ans)
        ns = list(map(int, input().split()))

solve()