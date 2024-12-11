#include <bits/stdc++.h>
using namespace std;

struct dot{
    int x;
    int y;
};

void solve(){
    int n; cin >> n;
    vector<dot> ds(n);
    for(auto &d:ds){
        int x, y;
        cin >> x >> y;
        d = {x, y};
    }

    int sum = 0;
    for(int i=1; i<n; ++i){
        sum += abs(ds[i].x-ds[i-1].x) + abs(ds[i].y-ds[i-1].y);
    }

    int ans = sum;
    for(int i=1; i<(n-1); ++i){
        int tmp = sum;
        tmp += abs(ds[i+1].x-ds[i-1].x)-abs(ds[i].x-ds[i-1].x)-abs(ds[i+1].x-ds[i].x);
        tmp += abs(ds[i+1].y-ds[i-1].y)-abs(ds[i].y-ds[i-1].y)-abs(ds[i+1].y-ds[i].y);
        ans = min(ans, tmp);
    }
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}