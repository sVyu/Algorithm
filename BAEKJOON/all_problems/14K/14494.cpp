#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    ll n, m; cin >> n >> m;
    int mod = int(1e9)+7;
    vector<vector<ll>> dp(n+1, vector<ll>(m+1, 0));

    dp[0][0] = 1;
    for(int i=1; i<=n; i++){
        for(int j=1; j<=m; j++){
            dp[i][j] = (dp[i-1][j-1]+dp[i-1][j]+dp[i][j-1]) % mod;
        }
    }

    cout << dp[n][m];
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}