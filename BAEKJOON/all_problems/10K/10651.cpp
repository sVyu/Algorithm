#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int ans = 0;
    ll n, t; cin >> n >> t;

    vector<ll> lis(n+1, -1);
    int lis_idx = 1;
    lis[0] = LLONG_MIN;

    for(ll i = 0; i < n; i++){
        ll x, y; cin >> x >> y;
        ll value = -(x+t*y);

        if(lis[lis_idx] <= value){
            lis[++lis_idx] = value;
        }else{
            int ti = upper_bound(lis.begin(), lis.begin()+lis_idx+1, value) - lis.begin();
            lis[ti] = value;
        }
        // for(int j = 0; j<= lis_idx; j++) cout << lis[j] << " ";
        // cout << "\n";
    }
    cout << lis_idx;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}