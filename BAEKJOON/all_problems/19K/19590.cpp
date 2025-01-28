#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int n; cin >> n;
    vector<int> zs(n); for(auto &z:zs) cin >> z;
    sort(zs.begin(), zs.end());

    ll sum = 0;
    int sz = zs.size();
    for(int i=0; i<(sz-1); ++i) sum += zs[i];

    ll ans = 0;
    if(sum < zs[sz-1])  ans = zs[sz-1]-sum;
    else                ans = (zs[sz-1]+sum)%2;

    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}