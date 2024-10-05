#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int mx = (1e5)+5;

void solve(){
    ll n, l; cin >> n >> l;
    vector<ll> sums(mx, 0);
    vector<ll> cnts(mx, 0);
    for(int i=0; i<n; i++){
        int c; cin >> c;
        cnts[c]++;
    }
    sums[0] = cnts[0];
    for(int i=1; i<mx; i++) sums[i] = sums[i-1]+cnts[i];

    ll lo=0, hi=n;
    ll ans=0;

    while(lo <= hi){
        ll mid = (lo+hi)/2;

        if((n-sums[mid]+min(cnts[mid], l)) >= (mid+1)){
            ans = mid+1;
            lo = mid+1;
        } else hi = mid-1;
    }

    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}