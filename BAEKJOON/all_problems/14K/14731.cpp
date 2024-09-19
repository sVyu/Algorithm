#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll mod = 1e9+7;

ll pw(ll n, ll k){
    if(k<=0) return 1;
    if(k==1) return n;

    if(k%2){
        return (n*pw(n, k-1)) % mod;
    }
    else{
        ll half_pw = pw(n, k/2);    //
        return (half_pw*half_pw) % mod;
    }
}

void solve(){
    ll ans = 0;
    int n; cin >> n;
    while(n--){
        ll c, k; cin >> c >> k;
        ans = (ans + c*((k*pw(2, k-1))%mod))%mod;
    }
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}