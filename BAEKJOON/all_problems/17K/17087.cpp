#include <bits/stdc++.h>
using namespace std;

int uc(int a, int b){
    if(b == 0) return a;
    return uc(b, a%b);
}

void solve(){
    int n, s; cin >> n >> s;
    int zs[n]; for(auto &z:zs) cin >> z;

    int vals[n];
    for(int i=0; i<n; ++i) vals[i] = abs(s-zs[i]);

    int ans = vals[0];
    for(int i=1; i<n; ++i) ans = uc(ans, vals[i]);

    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}