import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    for _ in range(n):
        dp = [0]*7
        dp[1] = 1

        for _ in range(int(input())):
            new_dp = [0]*7
            op1, val1, op2, val2, = input().rstrip().split()
            val1, val2 = int(val1), int(val2)
            # print(val1, val2)

            ops_and_vals = [[op1, val1], [op2, val2]]
            for i in range(7):
                if(dp[i]):
                    for op, val in ops_and_vals:
                        if(op == '+'):  new_dp[(i+val)%7] = 1
                        else:           new_dp[(i*val)%7] = 1
            dp = new_dp

        print("LUCKY" if dp[0] else "UNLUCKY")

solve()