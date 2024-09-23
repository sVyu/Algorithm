#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    if(n%2){
        cout << 0;
        return;
    }

    vector<int> dp(n+1, 0);
    dp[0]=1;

    for(int i=2; i<=n; i+=2){
        dp[i] += dp[i-2]*3;
        for(int j=4; j<=i; j+=2){
            dp[i] += dp[i-j]*2;
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