#include <bits/stdc++.h>
using namespace std;

void solve(){
    int c, n;
    cin >> c >> n;

    int sz=c+1;
    int dp[sz];
    fill(dp, dp+sz, 9999);
    dp[0]=0;

    while(n--){
        int k; cin >> k;
        for(int i=k; i<=c; i++){
            dp[i] = min(dp[i-k]+1, dp[i]);
        }
    }

    cout << dp[c];
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}