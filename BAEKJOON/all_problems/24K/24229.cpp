#include <bits/stdc++.h>
using namespace std;

struct lr{
    int l;
    int r;

    bool operator < (const lr _lr) const{
        if(l != _lr.l) return l < _lr.l;
        return r > _lr.r;
    }
};

void solve(){
    int n; cin >> n;
    vector<lr> lrs(n); // n
    for(auto &lr:lrs){
        int l, r; cin >> l >> r;
        lr = {l, r};
    }

    sort(lrs.begin(), lrs.end());
    int bl=0, br=0;
    int max_x=0;
    int ans=0; // = 0

    for(auto [l, r]:lrs){
        if(br >= l){
            br = max(br, r);
            max_x = max(max_x, br+(br-bl));
            ans = max(ans, br);
            continue; // 
        }

        if(max_x < l) continue;
        bl=l, br=r;
        max_x = max(max_x, br+(br-bl));
        ans = max(ans, br); 
    }

    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}