#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int n, m; cin >> n >> m;
    vector<int> zs(n); for(auto &z:zs) cin >> z;

    ll lo=1, hi=int(1e9);
    ll ans = -1;
    while(lo <= hi){
        ll mid = (lo+hi)/2;

        int cnt = 0, res = 0;
        for(auto z:zs){
            if(z > mid){
                cnt = m+1;
                break;
            }

            if(res >= z) res -= z;
            else{
                ++cnt;
                res = mid-z;
            }
        }

        if(cnt > m) lo = mid+1;
        else{
            ans = mid;
            hi = mid-1;
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