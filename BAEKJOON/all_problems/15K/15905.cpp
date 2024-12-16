#include <bits/stdc++.h>
using namespace std;

struct g{
    int n;
    int p;

    bool operator < (const g _g) const{
        if(n != _g.n) return n > _g.n;
        return p < _g.p;
    }
};

void solve(){
    int n; cin >> n;
    vector<g> gs(n); for(auto &g:gs){int n, p; cin >> n >> p; g = {n,p};}
    sort(gs.begin(), gs.end());

    int cnt=0;
    for(int i=5; i<n; ++i){
        if(gs[i].n == gs[4].n) cnt++;
        else break;
    }

    cout << cnt;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}