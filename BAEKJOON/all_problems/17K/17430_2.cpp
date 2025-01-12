#include <bits/stdc++.h>
using namespace std;

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

        set<int> xs, ys;
        for(auto d:dots){
            xs.insert(d.x);
            ys.insert(d.y);
        }

        bool is_balanced = (xs.size() * ys.size() == n);
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