import sys
input = sys.stdin.readline

def solve():
    scenario_cnt = int(input())

    mx = 50
    dp = [[0]*(mx) for _ in range(2)]
    dp[1][0] = 1

    for i in range(1, mx):
        dp[0][i] = dp[1][i-1]
        dp[1][i] = dp[0][i-1]+dp[1][i-1]

    # for x in range(2):
        # print(dp[x][:10])

    for scenario_num in range(1, scenario_cnt+1):
        n = int(input())
        print(f'Scenario {scenario_num}:')
        print(dp[0][n]+dp[1][n])

        if(scenario_num != scenario_cnt): print()

solve()