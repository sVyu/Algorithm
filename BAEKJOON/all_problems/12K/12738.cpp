#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    vector<int> zs(n); for(auto &z:zs) cin >> z;
    vector<int> lis(n, 0);

    lis[0] = zs[0];
    int lis_idx = 0;

    for(int i=1; i<n; ++i){
        if(lis[lis_idx] < zs[i]) lis[++lis_idx] = zs[i];
        else{
            int ti = lower_bound(lis.begin(), lis.begin()+lis_idx+1, zs[i])-lis.begin();
            lis[ti] = zs[i];
        }
    }
    cout << lis_idx+1;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}