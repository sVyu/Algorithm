#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// #define pli pair<ll, int>
struct vi{
    ll val;
    int idx;

    bool operator < (const vi _vi) const {
        if(val != _vi.val) return val < _vi.val;
        return idx > _vi.idx;
    }
};

void solve(){
    int n, d; cin >> n >> d;
    vector<ll> zs(n); for(auto &z:zs) cin >> z;
    zs.insert(zs.begin(), 0);

    ll dp[n+1];
    fill(dp, dp+n+1, -LLONG_MAX);
    dp[0] = 0;

    priority_queue<vi> pq;
    pq.push({0, 0});

    for(int i=1; i<=n; ++i){
        while(!pq.empty() and pq.top().idx < (i-d)) pq.pop();
        dp[i] = max(pq.top().val, 0LL)+zs[i]; // 최적화 가능
        pq.push({dp[i], i});
    }

    ll ans = -LLONG_MAX;
    for(int i=1; i<=n; ++i) ans = max(ans, dp[i]);
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}