#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int solve(){
    int n, m; cin >> n >> m;

    ll dp[m+1];
    fill(&dp[0], &dp[m+2], LLONG_MAX);

    while(n--){
        int k; cin >> k;
        ll min_val = LLONG_MAX;

        for(int i=m; i>=0; i--){
            if(dp[i] != LLONG_MAX){
                ll tmp_val = pow(m-i,2)+dp[i];      // pow(dp[i], 2)
                // min_val = min_val<tmp_val ? min_val : tmp_val;
                min_val = min(min_val, tmp_val);

                if(i <= (m-k-1)) dp[i+k+1] = dp[i];
                dp[i] = LLONG_MAX;
            }
        }

        dp[k] = min_val==LLONG_MAX? 0 : min_val;
    }

    ll ans = LLONG_MAX;
    for(int i=1; i<=m; i++) ans = min(ans, dp[i]);
    cout << ans;

    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}