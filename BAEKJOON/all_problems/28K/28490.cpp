#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    int ans = 0;

    while(n--){
        int h, w; cin >> h >> w;
        ans = max(ans, h*w);
    }
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}