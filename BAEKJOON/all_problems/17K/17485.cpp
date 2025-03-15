#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, m; cin >> n >> m;
    int board[n][m];
    for(int x=0; x<n; ++x) {
        for(int y=0; y<m; ++y){
            int k; cin >> k;
            board[x][y] = k;
        }
    }

    int mx = int(1e6);
    int dp[n][m][3];
    for(int x=0; x<n; ++x)
        for(int y=0; y<m; ++y)
            for(int i=0; i<3; ++i)
                dp[x][y][i] = mx;

    for(int y=0; y<m; ++y)
        for(int i=0; i<3; ++i)
            dp[0][y][i] = board[0][y];

    for(int x=1; x<n; ++x){
        for(int y=0; y<m; ++y){
            if(y>=1){
                for(int i=0; i<3; ++i){
                    if(i == 0) continue;
                    dp[x][y][0] = min(dp[x][y][0], dp[x-1][y-1][i]+board[x][y]);
                }
            }

            for(int i=0; i<3; ++i){
                if(i == 1) continue;
                dp[x][y][1] = min(dp[x][y][1], dp[x-1][y][i]+board[x][y]);
            }

            if(y<(m-1)){
                for(int i=0; i<3; ++i){
                    if(i == 2) continue;
                    dp[x][y][2] = min(dp[x][y][2], dp[x-1][y+1][i]+board[x][y]);
                }
            }
        }
    }

    int ans = mx;
    for(int y=0; y<m; ++y) for(int i=0; i<3; ++i) ans = min(ans, dp[n-1][y][i]);
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}