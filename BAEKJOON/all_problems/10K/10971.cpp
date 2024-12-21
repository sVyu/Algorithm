#include <bits/stdc++.h>
using namespace std;

void dfs(vector<vector<int>> &ws, vector<bool> &visited, int cnt, int s, int v, int n, int val, int &ans){
    if(cnt == (n-1)){
        if(ws[v][s] == 0) return; //
        ans = min(ans, val+ws[v][s]);
        return;
    }

    for(int i=0; i<n; ++i){
        if(visited[i]) continue;
        if(ws[v][i] == 0) continue; //
        visited[i] = true;
        dfs(ws, visited, cnt+1, s, i, n, val+ws[v][i], ans);
        visited[i] = false;
    }
}

void solve(){
    int n; cin >> n;
    vector<vector<int>> ws(n, vector<int>(n, 0));
    for(auto &r:ws) for(auto &el:r) cin >> el;
    vector<bool> visited(n, false);

    int ans = INT_MAX;
    int cnt = 0;
    for(int v=0; v<n; ++v)
    {
        visited[v] = true;
        dfs(ws, visited, cnt, v, v, n, 0, ans);
        visited[v] = false;
    }

    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}