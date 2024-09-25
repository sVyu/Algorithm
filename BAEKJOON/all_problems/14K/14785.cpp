#include <bits/stdc++.h>
using namespace std;

struct line{
    int s;
    int e;

    bool operator < (const line _line) const {
        if(s == _line.s) return e < _line.e;
        return s < _line.s;
    };
};

void solve(){
    int n; cin >> n;
    vector<line> lines(n);
    for(auto &l:lines){
        int s, len; cin >> s >> len;
        l = {s, s+len};
    }
    sort(lines.begin(), lines.end());

    int ans = 1;
    int e = INT_MAX;
    for(auto l:lines){
        if(e > l.s){
            e = min(e, l.e);
        } else{
            e = l.e;
            ans++;
        }
    }

    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie();
    solve();
    return 0;
}