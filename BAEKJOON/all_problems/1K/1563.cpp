#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    int mod = int(1e6);

    int dp[7][n+1];
    for(int x=0; x<7; ++x) for(int y=1; y<=n; ++y) dp[x][y] = 0;

    /*
        0. 출석 (지각 0)
        1. 출석 (지각 1)
        2. 지각 1
        3. 결석 1번 연속 (지각 0)
        4. 결석 1번 연속 (지각 1)
        5. 결석 2번 연속 (지각 0)
        6. 결석 2번 연속 (지각 1)
    */

    dp[0][1] = 1;
    dp[2][1] = 1;
    dp[3][1] = 1;

    for(int y=2; y<=n; ++y){
        dp[0][y] = (dp[0][y-1]+dp[3][y-1]+dp[5][y-1]) % mod;
        dp[1][y] = (dp[1][y-1]+dp[2][y-1]+dp[4][y-1]+dp[6][y-1]) % mod;
        dp[2][y] = (dp[0][y-1]+dp[3][y-1]+dp[5][y-1]) % mod;
        dp[3][y] = (dp[0][y-1]) % mod;
        dp[4][y] = (dp[1][y-1]+dp[2][y-1]) % mod;
        dp[5][y] = (dp[3][y-1]) % mod;
        dp[6][y] = (dp[4][y-1]) % mod;
    }

    int ans = 0;
    for(int x=0; x<7; ++x) ans += dp[x][n];
    ans %= mod;

    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}