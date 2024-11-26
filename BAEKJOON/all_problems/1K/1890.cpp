#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int n; cin >> n;
    vector<vector<int>> board(n, vector<int>(n));
    vector<vector<ll>> dp(n, vector<ll>(n, 0));
    for(auto &r:board) for(auto &el:r) cin >> el;

    dp[0][0] = 1;
    int dx[2] = {0, 1};
    int dy[2] = {1, 0};

    for(int x=0; x<n; ++x){
        for(int y=0; y<n; ++y){
            if(board[x][y] == 0) continue; //

            for(int d=0; d<2; ++d){
                int nx = x+board[x][y]*dx[d];
                int ny = y+board[x][y]*dy[d];
                if(nx >= n | ny >= n) continue;
                dp[nx][ny] += dp[x][y];
            }
        }
    }

    cout << dp[n-1][n-1];
}

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}