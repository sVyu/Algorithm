#include <bits/stdc++.h>
using namespace std;

struct vi{
    int val;
    int idx;
};

void solve(){
    int n, x, k; cin >> n >> x >> k;
    vector<int> zs(n); for(auto &z:zs) cin >> z;
    zs.insert(zs.begin(), 0);

    const int mx = int(2e6);
    vector<int> dp(n+1, mx);

    deque<vi> q;
    q.push_back({0, 0});

    int zero_cnt = 0;
    for(int i=1; i<=n; ++i){
        while(!q.empty() and q.front().idx < (i-x)){
            q.pop_front();
        }
        if(q.empty()){
            cout << -1;
            return;
        }

        if(zs[i] == 0)  zero_cnt++;
        else            zero_cnt = 0;

        int dp_val = q.front().val+1;
        if(zero_cnt >= k and q.front().idx <= (i-k)){
            q.push_back({dp_val, i});
        }

        dp[i] = dp_val;
    }

    cout << dp[n];
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}