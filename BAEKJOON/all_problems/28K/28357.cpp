#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    ll n, k; cin >> n >> k;
    vector<ll> zs(n); for(auto &z:zs) cin >> z;

    ll mx = ll(1e12);
    ll lo=0, hi=mx;
    ll ans = mx;
    while(lo<=hi){
        ll mid = (lo+hi)/2; // k
        ll sum = 0;

        for(auto z:zs) sum += max(z-mid, 0LL);
        if(sum <= k){
            ans = mid;
            hi = mid-1;
        }else{
            lo = mid+1;
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