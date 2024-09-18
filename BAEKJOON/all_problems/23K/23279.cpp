#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, k; cin >> n >> k;
    while(k--){
        int c; cin >> c;
        vector<int> zs(c); for(auto &z:zs) cin >> z;
        sort(zs.begin(), zs.end());

        for(int i=0; i<c; i++) cout << zs[i]+(i+1) << ' ';
        cout << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}