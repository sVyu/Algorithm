#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int n; cin >> n;
    vector<int> zs(n); for(auto &z:zs) cin >> z;
    ll p,q,r,s; cin >> p >> q >> r >> s;

    ll ans =-1;
    ll lo = 1, hi = int(2e5);

    while(lo <= hi){
        ll k = (lo+hi)/2; // mid
        ll sum = 0;

        for(auto z:zs){
            if(z > (k+r))   sum += (z-p);
            else if(z < k)  sum += (z+q);
            else            sum += z;
        }

        if(sum >= s){
            ans = k;
            hi = k-1;
        }else{
            lo = k+1;
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