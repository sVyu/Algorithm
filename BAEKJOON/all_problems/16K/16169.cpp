#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;

    vector<int> dots[n+2];  // idx -> 계급
    vector<int> work_times(n+1);
    vector<int> dp(n+1, 0); // time_dp, max로 갱신

    for(int i=1; i<=n; ++i){
        int c, t; cin >> c >> t;
        dots[c].push_back(i);
        work_times[i] = t;
    }

    for(int v:dots[1]){
        dp[v] = work_times[v];
    }

    for(int c=1; dots[c+1].size()>0; ++c){
        for(int v:dots[c]){
            for(int u:dots[c+1]){
                dp[u] = max(dp[u], dp[v]+(u-v)*(u-v)+work_times[u]);
            }
        }
    }

    // for(int d:dp) cout << d << ' ';
    cout << *max_element(dp.begin(), dp.end());
}

int main(void){
    ios::sync_with_stdio;
    cin.tie(0);
    solve();
    return 0;
}