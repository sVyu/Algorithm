#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int limit = int(1e6)+1;
    // int limit = int(1e5)+1;
    const ll mod = ll(1e9)+9;
    ll dp[limit];

    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;
    for(int i=4; i<limit; i++){
        dp[i] = (dp[i-1]+dp[i-2]+dp[i-3])%mod;
    }

    int n;
    cin >> n;
    int t;
    while(n--){
        cin >> t;
        cout << dp[t] << '\n';
    }

    return 0;
}