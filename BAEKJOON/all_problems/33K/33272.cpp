#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, m, k; cin >> n >> m >> k;
    vector<int> ans;
    set<int> visited;

    int len_ans = 0;
    for(int t=1; t<=m; ++t){
        if(visited.count(t) <= 0){
            visited.insert(t);
            visited.insert(t^k);
            ans.push_back(t);
            if(ans.size() >= n) break;
        }
    }

    if(ans.size() >= n){
        for(auto val:ans) cout << val << ' ';
        return;
    }
    cout << -1;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}