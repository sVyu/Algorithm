#include <bits/stdc++.h>
using namespace std;

const int mx_p_size = 1e6+1;

void solve(){
    int m, n; cin >> m >> n;

    map<vector<int>, int> mzip_vp;
    int ans = 0;
    while(m--){
        vector<int> vp(n);  for(auto &p:vp) cin >> p;
        set<int> sp;        for(auto p:vp) sp.insert(p);
        vector<int> sorted_sp(sp.begin(), sp.end()); 
        sort(sorted_sp.begin(), sorted_sp.end());

        // map<int, int> map_p;
        // for(int i=0; i<sorted_sp.size(); i++) map_p[sorted_sp[i]] = i;

        vector<int> zip_vals(mx_p_size, 0);
        for(int i=0; i<sorted_sp.size(); i++) zip_vals[sorted_sp[i]] = i;

        vector<int> zip_vp(n);
        for(int i=0; i<n; i++) zip_vp[i] = zip_vals[vp[i]];

        ans += mzip_vp[zip_vp]++;
    }
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}