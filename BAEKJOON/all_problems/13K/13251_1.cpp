// 2024.09.06 19:11 ~ 19:24 (WA)
#include <bits/stdc++.h>
#include <numeric>
using namespace std;
typedef long long ll;

ll f(ll n){
    ll v=1;
    for(ll k=2; k<=n; k++) v*=k;
    return v;
}

ll c(ll n, ll k){
    ll v=1;
    for(ll i=n; i>(n-k); i--) v*=i;
    return v/f(k);
}

void solve(){
    int m; cin >> m;
    // ll zs[m]; for(auto &z:zs) cin >> z;
    vector<ll> zs(m); for(auto &z:zs) cin >> z;
    ll k; cin >> k;

    ll all_cnt=0;
    for(auto z:zs) all_cnt += c(z,k);

    cout.precision(15);
    cout << (long double)all_cnt/c(accumulate(zs.begin(), zs.end(), 0LL), k);
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}