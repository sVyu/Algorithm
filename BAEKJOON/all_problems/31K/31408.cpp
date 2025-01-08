#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    int mx = int(1e5);
    vector<int> cnts(mx+1, 0);

    for(int i=0; i<n; ++i){
        int k; cin >> k;
        ++cnts[k];
    }

    int limit = (n/2)+(n%2);
    for(int i=1; i<=mx; ++i){
        if(cnts[i] > limit){
            cout << "NO";
            return;
        }
    }

    cout << "YES";
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}