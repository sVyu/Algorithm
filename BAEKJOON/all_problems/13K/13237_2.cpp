#include <bits/stdc++.h>
using namespace std;

int dfs(vector<int> &ps, int lvs[], int v){
    if(lvs[v] == 0 and ps[v] >= 0){
        lvs[v] = dfs(ps, lvs, ps[v])+1;
    }
    return lvs[v];
}

void solve(){
    int n; cin >> n;
    vector<int> ps(n, 0);
    for(auto &p:ps){
        int k; cin >> k;
        p = k-1;
    }

    int lvs[n]{};
    for(int v=0; v<n; v++) dfs(ps, lvs, v);
    for(auto lv:lvs) cout << lv << '\n';
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}