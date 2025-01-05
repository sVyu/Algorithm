#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    vector<int> zs(n); for(auto &z:zs) cin >> z;
    vector<int> sums(n+1);
    for(int i=1; i<=n; ++i) sums[i] = sums[i-1] + zs[i-1];

    int l=1, r=1;
    int ans = -1;
    while(r <= n){
        int in_gap = sums[r]-sums[l-1];
        int out_gap = (sums[n]-sums[r])+sums[l-1];

        ans = max(ans, min(in_gap, out_gap));
        if(in_gap < out_gap){
            ++r;
        }else{
            ++l;
            if(l > r) ++r;
        }
    }

    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}