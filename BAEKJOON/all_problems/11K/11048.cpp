#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, m; cin >> n >> m;
    vector<vector<int>> board(n, vector<int>(m, 0));
    vector<vector<int>> dp(n, vector<int>(m, 0));
    for(auto &r:board) for(auto &el:r) cin >> el;

    for(int x=0; x<n; ++x){
        for(int y=0; y<m; ++y){
            if(x-1 >= 0)                dp[x][y] = max(dp[x][y], dp[x-1][y]);
            if(y-1 >= 0)                dp[x][y] = max(dp[x][y], dp[x][y-1]);
            if(x-1 >= 0 and y-1 >= 0)   dp[x][y] = max(dp[x][y], dp[x-1][y-1]);
            dp[x][y] += board[x][y];
        }
    }

    cout << dp[n-1][m-1];
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}