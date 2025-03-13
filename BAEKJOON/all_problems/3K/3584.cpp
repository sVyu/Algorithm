#include <bits/stdc++.h>
using namespace std;

void dfs(int v, vector<int> g[], int levels[], int parents[]){
    for(int u:g[v]){
        levels[u] = levels[v]+1;
        parents[u] = v;
        dfs(u, g, levels, parents);
    }
}

void solve(){
    int t; cin >> t;
    while(t--){
        int n; cin >> n;

        bool root_check[n+1] = {false,};
        for(int i=1; i<=n; ++i) root_check[i] = true;

        vector<int> g[n+1];
        for(int i=0; i<(n-1); ++i){
            int a, b; cin >> a >> b;
            g[a].push_back(b);
            root_check[b] = false;
        }

        int root = -1;
        for(int i=1; i<=n; ++i) if(root_check[i]) root = i;

        int levels[n+1];
        int parents[n+1];
        fill(levels, levels+n+1, -1);
        fill(parents, parents+n+1, -1);

        levels[root] = 0;
        dfs(root, g, levels, parents);

        // for(auto lv:levels) cout << lv << ' ';
        // for(auto p:parents) cout << p << ' ';

        int a, b; cin >> a >> b;
        while(levels[a] > levels[b]) a = parents[a];
        while(levels[a] < levels[b]) b = parents[b];

        while(a != b){
            a = parents[a];
            b = parents[b];
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