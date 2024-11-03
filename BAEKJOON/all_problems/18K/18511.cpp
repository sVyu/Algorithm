#include <bits/stdc++.h>
using namespace std;

int ans=-1;

void rec(vector<int> &zs, int val, int len, int max_len, int n, int k){
    if(len <= max_len){
        if(val <= n) ans = max(ans, val);
        if(len == max_len) return;
    }

    for(int i=0; i<k; i++){
        rec(zs, val*10+zs[i], len+1, max_len, n, k);
    }
}

void solve(){
    int n, k; cin >> n >> k;
    vector<int> zs(k); for(auto &z:zs) cin >> z;

    int max_len = to_string(n).length();
    rec(zs, 0, 0, max_len, n, k);
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}