import sys
input = sys.stdin.readline

def solve():
    for _ in range(int(input())):
        n, k = map(int, input().split())        
        # print(val)

        val = int('1'*n)
        ans = []

        while(k):
            quo = min(9, k//val)
            if(quo > 0):
                ans.append(quo*val)
                k -= quo*val
            else:
                val //= 10

        print(len(ans))
        print(*ans)

solve()