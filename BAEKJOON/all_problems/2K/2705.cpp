#include <bits/stdc++.h>
using namespace std;

void solve(){
    int a, b; cin >> a >> b;
    int t; cin >> t;
    while(t--){
        int val; cin >> val;
        cout << val << ' ' << min(val, 1000)*a + max(val-1000, 0)*b << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}