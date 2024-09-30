#include <bits/stdc++.h>
using namespace std;

const int mx = INT_MAX;

void solve(){
    int n, m, t; cin >> n >> m >> t;

    vector<vector<int>> dists(n+1, vector<int>(n+1, 0));
    while(m--){
        int u, v, h; cin >> u >> v >> h;
        dists[u][v] = max(dists[u][v], h);
    }
    for(auto &d:dists) for(auto &e:d) if(e==0) e=mx;

    for(int k=0; k<=n; k++){
        for(int i=0; i<=n; i++){
            for(int j=0; j<=n; j++){
                dists[i][j] = min(dists[i][j], max(dists[i][k], dists[k][j]));
            }
        }
    }

    while(t--){
        int s, e;
        cin >> s >> e;
        if(dists[s][e] == mx){
            cout << -1 << '\n';
            continue;
        }
        cout << dists[s][e] << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}