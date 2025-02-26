#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

bool dfs(vector<int> g[], int v, int target){
    if(v == target) return true;

    bool has_found = false;
    for(auto u:g[v]){
        has_found |= dfs(g, u, target);
        if(has_found) break;
    }

    return has_found;
}

void solve(){
    int n, m; cin >> n >> m;
    vector<int> g[n+1];

    while(m--){
        int x, y; cin >> x >> y;
        g[x].push_back(y);
    }

    int p, q; cin >> p >> q;
    if(dfs(g, p, q)){
        cout << "yes";
        return;
    }
    else if(dfs(g, q, p)){
        cout << "no";
        return;
    }
    cout << "unknown";
    return;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}