#include <bits/stdc++.h>
using namespace std;

void solve(){
    int t; cin >> t;
    while(t--){
        int ans = 0;
        int n; cin >> n;
        while(n--){
            int a, b, c; cin >> a >> b >> c;
            ans += max(0, max(max(a, b), c));
        }
        cout << ans << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}