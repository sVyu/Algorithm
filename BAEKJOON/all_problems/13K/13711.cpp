#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    vector<int> nas(n); for(auto &a:nas) cin >> a;
    vector<int> nbs(n); for(auto &b:nbs) cin >> b;

    vector<int> idx_table(n+1);
    for(int i=0; i<n; i++) idx_table[nas[i]] = i;

    vector<int> lis(n, int(1e6));
    lis[0] = idx_table[nbs[0]];
    int max_lis_idx = 0;

    for(int i=1; i<n; i++){
        if(lis[max_lis_idx] < idx_table[nbs[i]])
            lis[++max_lis_idx] = idx_table[nbs[i]];
        else{
            int target_idx = lower_bound(lis.begin(), lis.end(), idx_table[nbs[i]])-lis.begin();
            lis[target_idx] = idx_table[nbs[i]];
        }
    }

    cout << max_lis_idx+1;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}