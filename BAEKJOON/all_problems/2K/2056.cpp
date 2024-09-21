#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    vector<int> pre_cnts(n+1, 0);
    vector<vector<int>> g(n+1);
    vector<int> vals(n+1, 0);
    vector<int> tot_vals(n+1, 0);

    for(int v=1; v<=n; v++){
        int val; cin >> val;
        vals[v] = val;

        int k; cin >> k;
        while(k--){
            int u; cin >> u;
            g[u].push_back(v);  //
            pre_cnts[v]++;      //
        }
    }

    queue<int> q;
    for(int v=1; v<= n; v++){
        if(pre_cnts[v] == 0){
            q.push(v);
            tot_vals[v] = vals[v];
        }
    }

    while(!q.empty()){
        int v = q.front(); q.pop();
        for(auto u:g[v]){
            tot_vals[u] = max(tot_vals[u], tot_vals[v]+vals[u]);
            if(--pre_cnts[u] == 0) q.push(u);
        }
    }

    cout << *max_element(tot_vals.begin()+1, tot_vals.end());
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}