#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    vector<int> zs(n); for(auto &z:zs) cin >> z;
    zs.insert(zs.begin(), 0);
    vector<vector<int>> dp(2, vector<int>(n+1, 0));

    for(int i=1; i<=n; ++i){
        if(zs[i] == 1){
            dp[0][i] = dp[0][i-1]+1;
            dp[1][i] = max(0, dp[1][i-1]-1);
        }
        else{
            dp[0][i] = max(0, dp[0][i-1]-1);
            dp[1][i] = dp[1][i-1]+1;
        }
    }

    int ans = 0;
    for(int i=1; i<=n; ++i){
        ans = max(ans, max(dp[0][i], dp[1][i]));
    }
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}