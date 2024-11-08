#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int z; cin >> z;
    while(z--){
        int n; cin >> n;
        vector<ll> zs(n, 0); for(auto &z:zs) cin >> z;
        if(n <= 2){
            cout << *max_element(zs.begin(), zs.end()) << '\n';
            continue;
        }

        vector<ll> dp(n, 0);
        for(int i=0; i<2; i++) dp[i] = zs[i];
        for(int i=2; i<n; i++){
            dp[i] = max(zs[i], dp[i-2]+zs[i-1]+zs[i]);
        }

        cout << *max_element(dp.begin(), dp.end()) << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}