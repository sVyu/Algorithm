#include <bits/stdc++.h>
using namespace std;

void dfs(vector<vector<int>> &g, vector<string> &ss, vector<bool>& visited, string& ans, int v){
    visited[v] = true;
    ans += ss[v];
    for(auto u:g[v]){
        if(!visited[u]){
            dfs(g, ss, visited, ans, u);
        }
    }
}

void solve(){
    int n; cin >> n;
    vector<string> ss(n); for(auto &s:ss) cin >> s;
    vector<vector<int>> g(n);
    vector<vector<int>> rev_g(n);

    for(int i=1; i<n; ++i){
        int a, b;
        cin >> a >> b;
        a -= 1; b -= 1;
        g[a].push_back(b);
        rev_g[b].push_back(a);
    }

    int root = -1;
    for(int i=0; i<n; ++i){
        if(rev_g[i].size() == 0) root = i;
    }
    // cout << root;

    vector<bool> visited(n, false);
    string ans = "";
    dfs(g, ss, visited, ans, root);
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}