#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, m; cin >> n >> m;
    int sz=1000;
    vector<int> zs1(sz,0), zs2(sz,0);

    for(int i=0; i<n; i++) cin >> zs1[i];
    for(int i=0; i<m; i++) cin >> zs2[i];

    int ans=0;
    for(int i=0; i<sz; i++){
        ans = max(ans, zs2[i]-zs1[i]);
    }
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}