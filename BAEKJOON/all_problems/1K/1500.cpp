#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int s, k; cin >> s >> k;

    vector<ll> zs(k, 0);
    for(int i=0; i<s; ++i){
        ++zs[i%k];
    }

    ll ans = 1;
    for(auto z:zs) ans *= z;
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}