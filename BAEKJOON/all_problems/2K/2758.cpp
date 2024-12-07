#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(void){
    // dp table init
    int mxn = 10, mxm = 2000;
    vector<vector<ll>> dp(mxm+1, vector<ll>(mxn+1, 0));
    for(int x=1; x<=mxm; ++x) dp[x][0] = 1;

    for(int y=0; y<(mxn-1); ++y){
        for(int x=(mxm/2); x>=1; --x){
            if(dp[x][y] == 0) break;
            for(int k=(2*x); k<=mxm; ++k) dp[k][y+1] += dp[x][y];
        }
    }

    // take input values -> calc & cout ans
    int t; cin >> t;
    while(t--){
        int n, m; cin >> n >> m;
        ll ans = 0;
        for(int x=(1<<(n-1)); x<=m; ++x) ans += dp[x][n-1];
        cout << ans << '\n';
    }

    return 0;
}