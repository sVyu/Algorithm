#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int n; cin >> n;

    const int sz = 1001;
    vector<int> cnts(sz, 0);
    ll jinju_cost = -1;

    for(int i=0; i<n; i++){
        string s; ll val;
        cin >> s >> val;

        if(s == "jinju") jinju_cost = val;
        if(val < sz) cnts[val]++;
    }

    ll cnt = 0;
    for(int i=1; i<=jinju_cost; i++) cnt += cnts[i];
    cout << jinju_cost << '\n' << n-cnt;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}