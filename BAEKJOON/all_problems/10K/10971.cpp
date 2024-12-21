#include <bits/stdc++.h>
using namespace std;

void dfs(vector<vector<int>> &ws, vector<bool> &visited, int cnt, int s, int i, int n, int val, int &ans){
    if(cnt == (n-1)){
        if(ws[i][s] == 0) return; //
        ans = min(ans, val+ws[i][s]);
        return;
    }

    for(int j=0; j<n; ++j){
        if(visited[j]) continue;
        if(ws[i][j] == 0) continue; //
        visited[j] = true;
        dfs(ws, visited, cnt+1, s, j, n, val+ws[i][j], ans);
        visited[j] = false;
    }
}

void solve(){
    int n; cin >> n;
    vector<vector<int>> ws(n, vector<int>(n, 0));
    for(auto &r:ws) for(auto &el:r) cin >> el;
    vector<bool> visited(n, false);

    int ans = INT_MAX;
    int cnt = 0;
    for(int i=0; i<n; ++i)
    {
        visited[i] = true;
        dfs(ws, visited, cnt, i, i, n, 0, ans);
        visited[i] = false;
    }

    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}