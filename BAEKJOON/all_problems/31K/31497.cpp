#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    vector<string> ss(n); for(auto &s:ss) cin >> s;

    while(n--){
        for(int i=0; i<2; ++i){
            cout << "? " << ss[n] << endl; // endl -> cout + flush
            int ans; cin >> ans;
            if(ans == 1){
                cout << "! " << ss[n];
                return;
            }
        }
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}