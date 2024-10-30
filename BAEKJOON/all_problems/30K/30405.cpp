#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int n, m; cin >> n >> m;
    vector<int> xs(m+1, 0);
    for(int i=0; i<n; i++){
        int k; cin >> k;
        vector<int> zs(k); for(auto &z:zs) cin >> z;
        xs[zs[0]]++;
        xs[zs[k-1]]++;
    }

    ll res = accumulate(xs.begin(), xs.end(), 0LL);
    ll tot=0;
    ll left=0;

    ll min_val = LLONG_MAX;
    int ans = 0;

    for(int i=1; i<=m; i++){
        tot -= res;
        tot += left;

        res -= xs[i];
        left += xs[i];

        if(min_val > tot){
            min_val = tot;
            ans = i;
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