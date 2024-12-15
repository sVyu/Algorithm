#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(void){
    int n; cin >> n;
    vector<int> zs(n); for(auto &z:zs) cin >> z;
    sort(zs.begin(), zs.end(), less<int>());
    // for(auto z:zs) cout << z << ' ';
    // cout << '\n';

    ll s = accumulate(zs.begin(), zs.end(), 0LL);
    ll ans = s;
    for(auto z:zs){
        if((-s) > z){
            ans += -s-z;
            s = -z;
        }
    }
    cout << ans;

    return 0;
}