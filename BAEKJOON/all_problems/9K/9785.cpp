#include <bits/stdc++.h>
using namespace std;

struct dot {
    int a;
    int b;

    bool operator < (const dot _dot) const{
        if(a != _dot.a) return a > _dot.a;
        else return b > _dot.b;
    }
};

void solve(){
    int n, m; cin >> n >> m;
    vector<dot> dots(n);
    for(int i=0; i<n; i++){
        int a, b; cin >> a >> b;
        dots[i] = {a, b};
    }

    stable_sort(dots.begin(), dots.end());

    int ans_a=0, ans_b = INT_MAX;
    for(int i=0; i<m; i++){
        auto [a, b] = dots[i];
        ans_a += a;
        ans_b = min(ans_b, b);
    }
    cout << ans_a << ' ' << ans_b << '\n';
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}