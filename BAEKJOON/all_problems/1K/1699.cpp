#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;

    vector<int> dp(n+1, 0);
    for(int i=1; i<=n; i++) dp[i] = i;

    int sqrt_n = int(sqrt(n));
    for(int i=2; i<=sqrt_n; i++){
        int sq_i = i*i;
        if(sq_i > n) break;

        for(int k=sq_i; k<=n; k++){
            dp[k] = min(dp[k], dp[k-sq_i]+1);
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