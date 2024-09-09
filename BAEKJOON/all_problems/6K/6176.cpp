#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, m; cin >> n >> m;
    vector<int> sum(n+1, m);
    for(int i=1; i<=n; i++){
        int k; cin >> k;
        sum[i] = sum[i-1]+k;
    }
    sum[0]=0;

    int MX = INT_MAX;
    vector<int> dp(n+1, MX);
    dp[0] = 0;

    for(int i=1; i<=n; i++){
        dp[i] = sum[i];
        for(int j=0; j<i; j++){
            dp[i] = min(dp[i], dp[j]+sum[i-j]+m);
        }
    }
    cout << dp[n];
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}