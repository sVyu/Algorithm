#include <bits/stdc++.h>
using namespace std;

/*
    2 1
    2 -1
*/

struct dot{
    int x;
    int y;
};

void solve(){
    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        vector<dot> dots(n);
        for(auto &d:dots){int x, y; cin >> x >> y; d = {x, y};}

        map<int, set<int>> mapx;
        set<int> xs;

        for(auto d:dots){
            mapx[d.x].insert(d.y);
            xs.insert(d.x);
        }
        // cout << (int)*xs.begin();

        set<int> res = mapx[*xs.begin()];
        for(auto &x:xs){
            set<int> tmp;
            set_intersection(mapx[x].begin(), mapx[x].end(), res.begin(), res.end(), inserter(tmp, tmp.begin()));
            res = tmp;
        }

        bool is_balanced = (res.size() == mapx[*xs.begin()].size());
        if(is_balanced) cout << "BALANCED\n";
        else            cout << "NOT BALANCED\n";
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}