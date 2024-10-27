#include <bits/stdc++.h>
using namespace std;

struct pt{
    int k;
    int x;
    int y;
};

bool cmp(pt a, pt b){
    if(a.x == b.x) return a.y < b.y;
    return a.x < b.x;
}

void solve(){
    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        vector<pt> pts;
        for(int i=1; i<=n; i++){
            int x, y; cin >> x >> y;
            pts.push_back({i, x, y});
        }

        sort(pts.begin(), pts.end(), cmp);
        for(auto _pt:pts){
            cout << _pt.k << ' ' << (_pt.x+1) << ' ' << (_pt.y+int(3e8)) << '\n';
        }
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}