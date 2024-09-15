#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        vector<ll> zs(n); for(auto &z:zs) cin >> z;
        reverse(zs.begin(), zs.end());

        ll mx=-1, ans=0;
        for(auto z:zs){
            mx = max(mx, z);
            ans += (mx-z);
        }
        cout << ans << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}