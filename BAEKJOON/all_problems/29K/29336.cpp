#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int n, m; cin >> n >> m;
    vector<int> zs(n); for(auto &z:zs) cin >> z;
    sort(zs.begin(), zs.end(), greater<int>());

    // for(auto z:zs) cout << z;
    int zi=0;
    int t, q;
    ll ans = 0;

    // while(m--){
    for(int i=0; i<m; ++i){
        cin >> t >> q;
        while(zi<n and ans < q){
            ans += zs[zi++]+t;
        }
        // cout << m << ' ' << ans << ' ' << q << '\n';
        if(ans < q){
            cout << -1;
            return;
        }
    }

    while(zi<n){
        ans += zs[zi++]+t;
    }
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}