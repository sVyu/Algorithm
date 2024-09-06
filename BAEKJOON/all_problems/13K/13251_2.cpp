#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int m; cin >> m;
    vector<int> zs(m); for(auto &z:zs) cin >> z;
    int tot = accumulate(zs.begin(), zs.end(), 0);
    int k; cin >> k;
    
    double ans = 0;
    for(auto z:zs){
        if(z<k) continue;
        double val = 1;
        int t=tot;
        for(int i=k; i>0; i--) val *= (double)z--/t--;  //
        ans += val;
    }

    cout.precision(10);
    cout << ans << '\n';
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}