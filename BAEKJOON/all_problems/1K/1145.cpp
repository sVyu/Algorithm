#include <bits/stdc++.h>
using namespace std;

void solve(){
    vector<int> zs(5, 0); for(auto &z:zs) cin >> z;

    int n=1;
    while(n < int(1e9)){
        int cnt=0;
        for(auto z:zs) if((n%z) == 0) cnt++;
        if(cnt >= 3){
            cout << n;
            return;
        }
        n++;
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}