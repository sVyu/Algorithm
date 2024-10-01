#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    vector<int> zs(n); for(auto &z:zs) cin >> z;
    reverse(zs.begin(), zs.end());

    int now=2e4;
    int ans = 0;
    for(auto z:zs){
        if(now <= z){
            ans += (z-now+1);
        }
        now = min(now-1, z);
    }
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}