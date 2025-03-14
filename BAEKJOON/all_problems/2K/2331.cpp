#include <bits/stdc++.h>
using namespace std;

int cal(int a, int p){
    int val = 0;
    while(a){
        int k = 1;
        for(int i=0; i<p; ++i) k *= a%10;
        val += k;
        a /= 10;
    }
    return val;
}

void solve(){
    int a, p;
    cin >> a >> p;

    const int mx = int(5e5);
    int cnts[mx] = {0, };

    int val = a;
    while(cnts[val] < 2){
        ++cnts[val];
        val = cal(val, p);
        // cout << val << '\n';
    }

    int ans = 0;
    for(int i=1; i<mx; ++i) if(cnts[i] == 1) ++ans;
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}