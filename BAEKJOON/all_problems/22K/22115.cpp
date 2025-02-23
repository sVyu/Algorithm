#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, k; cin >> n >> k;
    vector<int> zs(n); for(auto &z:zs) cin >> z;

    int inf = int(1e9);
    int dp[k+1];
    fill(dp, dp+(k+1), inf);
    dp[0] = 0;

    for(int z:zs){
        for(int i=k; i>=z; i--){ //
            if(dp[i-z] != inf)
                dp[i] = min(dp[i], dp[i-z]+1);
        }
    }

    // for(int i=0; i<k; ++i) cout << dp[i] << ' ';
    int ans = (dp[k] < inf) ? dp[k] : -1; //
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}