#include <bits/stdc++.h>
using namespace std;

int inf = INT_MAX-1;

int solve(){
    int tc; cin >> tc;
    while(tc--){
        int target; cin >> target;
        int max_val = 1e4;
        int dp[max_val+1];
        fill(dp, dp+max_val+2, inf);

        int n; cin >> n;
        while(n--){
            int v; cin >> v;
            for(int i=max_val-v; i >= 0; i--){          // i > v (x) -> i >= 0 (o)
                dp[i+v] = min(dp[i+v], dp[i]+1);        // MAX_INT+1 -> overflow
            }
            dp[v] = 1;
        }

        for(int i=target; i <= max_val; i++){
            if(dp[i] == inf) continue;
            cout << i << ' ' << dp[i] << '\n';
            break;
        }
    }
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}