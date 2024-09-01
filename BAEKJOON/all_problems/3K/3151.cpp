#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int n; cin >> n;
    vector<int> zs(n,0);
    for(auto &z:zs) cin >> z;
    sort(zs.begin(), zs.end());

    ll ans = 0;
    for(int i=0; i<n-2; i++){
        for(int j=i+1; j<n-1; j++){
            int val = zs[i]+zs[j];
            vector<int>::iterator s = zs.begin()+j+1;
            ans += upper_bound(s, zs.end(), -val)-lower_bound(s, zs.end(), -val);
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