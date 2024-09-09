#include <bits/stdc++.h>
using namespace std;

void solve(){
    int t; cin >> t;
    cout << t;
    while(t--){
        int n; cin >> n;
        vector<int> zs(n); for(auto &z:zs) cin >> z;

        sort(zs.begin(), zs.end());
        swap(zs[0], zs[1]);

        cout << "\n\n" << n << '\n';
        for(auto z:zs) cout << z << ' ';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}