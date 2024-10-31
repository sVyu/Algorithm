#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    ll n, m, k; cin >> n >> m >> k;
    ll ans=0;

    vector<ll> zs(n, 0);
    for(int i=0; i<n; i++){
        ll mi; cin >> mi;
        ll cnt = min(mi/m, k), res = mi%m;
        k -= cnt;
        ans += m*cnt;
        zs[i] = res;
        if(k == 0) break;
    }

    if(k>0){
        sort(zs.begin(), zs.end());
        for(int i=(n-1); i>=0; i--){
            ans += zs[i];
            if(--k == 0) break;
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