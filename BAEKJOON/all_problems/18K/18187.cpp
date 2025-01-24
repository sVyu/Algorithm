#include <bits/stdc++.h>
using namespace std;

/*
plus_val
1 2 3
3 4 5
5 6 7
7
*/

void solve(){
    int n; cin >> n;
    int ans = 1, val = 1;

    for(int cnt=1; cnt<=n; ++cnt){
        ans += val;
        if(cnt % 3) val++;
    }

    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}