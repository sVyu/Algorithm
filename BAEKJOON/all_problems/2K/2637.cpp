#include <bits/stdc++.h>
using namespace std;

struct e{
    int v;
    int weight;
};

void solve(){
    int n, m; cin >> n >> m;
    vector<int> weights(n+1, 0);
    vector<int> pre_cnts(n+1, 0);
    vector<bool> base_part(n+1, true);
    vector<vector<e>> g(n+1);

    for(int i=0; i<m; i++){
        int x, y, k; cin >> x >> y >> k;
        g[x].push_back({y, k});
        base_part[x] = false;
        pre_cnts[y] += 1;
    }

    queue<e> flows;
    for(int v=1; v<=n; v++){
        if(pre_cnts[v] == 0) flows.push({v, 1});
    }

    while(!flows.empty()){
        auto [v, w] = flows.front(); flows.pop();
        for(auto [u, nw]:g[v]){
            weights[u] += w*nw;
            if(--pre_cnts[u] == 0){
                flows.push({u, weights[u]});
                // flows.push({u, tw});
            }
        }
    }

    for(int v=1; v<=n; v++){
        if(base_part[v]) cout << v << ' ' << weights[v] << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}