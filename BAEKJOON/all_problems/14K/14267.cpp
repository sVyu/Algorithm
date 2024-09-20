#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void dfs(ll v, ll val, vector<vector<ll>>& g, vector<ll>& vals, vector<ll>& ans){
    val += vals[v];
    ans[v] = val;
    for(auto u:g[v]){
        dfs(u, val, g, vals, ans);
    }
}

void solve(){
    ll n, m; cin >> n >> m;
    ll root = -1;
    vector<vector<ll>> g(n);
    for(ll i=0; i<n; i++){
        ll k; cin >> k;
        if(k==-1){
            root = i;
            continue;
        }
        g[k-1].push_back(i);
    }

    vector<ll> vals(n, 0);
    while(m--){
        ll i, w; cin >> i >> w;
        vals[i-1] += w;
    }

    vector<ll> ans(n, 0);
    dfs(root, 0LL, g, vals, ans);
    for(auto a: ans) cout << a << ' ';
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}