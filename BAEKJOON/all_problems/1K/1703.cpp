#include <bits/stdc++.h>
using namespace std;

void solve(){
    int a; cin >> a;
    while(a){
        unsigned int ans = 1;
        for(int i=0; i<a; ++i){
            int m, n; cin >> m >> n;
            ans = ans*m-n;
        }

        cout << ans << '\n';
        cin >> a;
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}