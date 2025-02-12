#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    vector<int> zs(n); for(auto &z:zs) cin >> z;
    int dp[n]={1,};

    for(int i=1; i<n; ++i){
        dp[i] = min(zs[i], dp[i-1]+1);
    }

    int ans = 0;
    for(int i=0; i<n; ++i) ans = max(ans, dp[i]);

    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}