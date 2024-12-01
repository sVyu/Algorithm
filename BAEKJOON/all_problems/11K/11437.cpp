#include <bits/stdc++.h>
using namespace std;

void dfs(int p, int v, vector<vector<int>>& g, vector<int>& acsts, vector<int>& lvs, int lv){
    lvs[v] = lv;
    for(auto u:g[v]){
        if(p == u) continue;
        acsts[u] = v;
        dfs(v, u, g, acsts, lvs, lv+1);
    }
}

void solve(){
    int n; cin >> n;
    int mx = int(5e4+1);
    vector<vector<int>> g(mx, vector<int>());
    // while(n--){
    while(--n){
        int a, b; cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }

    vector<int> acsts(mx, 1);
    vector<int> lvs(mx, 1);
    dfs(0, 1, g, acsts, lvs, 1);

    int m; cin >> m;
    while(m--){
        int a, b; cin >> a >> b;
        while(lvs[a] > lvs[b]) a = acsts[a];
        while(lvs[a] < lvs[b]) b = acsts[b];
        while(a != b){
            a = acsts[a];
            b = acsts[b];
        }
        cout << a << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}