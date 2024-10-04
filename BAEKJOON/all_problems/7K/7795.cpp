#include <bits/stdc++.h>
using namespace std;

void solve(){
    int t; cin >> t;
    while(t--){
        int n, m; cin >> n >> m;
        vector<int> zs1(n); for(auto &z:zs1) cin >> z;
        vector<int> zs2(m); for(auto &z:zs2) cin >> z;
        sort(zs1.begin(), zs1.end());
        sort(zs2.begin(), zs2.end());

        int i1 = 0, i2 = 0;
        int ans = 0;
        while(i1<n and i2<m){
            if(zs1[i1] > zs2[i2]){
                while((i2+1)<m and zs1[i1] > zs2[i2+1]) i2++;
                ans += (i2+1);
            }
            i1++;
        }
        cout << ans << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}