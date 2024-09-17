#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int n; cin >> n;
    vector<ll> zs(n); for(auto &z:zs) cin >> z;
    sort(zs.begin(), zs.end());
    set<ll> set_sums{};

    ll ans = 0;
    for(int i=0; i<n; i++){
        for(int j=0; j<=i; j++){
            set_sums.insert(zs[i]+zs[j]);
        }

        for(int j=i+1; j<n; j++){
            if(set_sums.count(zs[j]-zs[i])){
                ans = max(ans, zs[j]);
            }
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