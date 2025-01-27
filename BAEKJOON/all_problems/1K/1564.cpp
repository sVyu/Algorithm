#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int n; cin >> n;

    int cnts[2]={0,0}; // 2, 5 cnts
    ll val = 1;
    ll mod = ll(1e5);

    for(ll i=1; i<=n; ++i){
        ll ti = i;
        while(ti%2 == 0){
            ++cnts[0];
            ti /= 2;
        }
        while(ti%5 == 0){
            ++cnts[1];
            ti /= 5;
        }
        val = (val*ti)%mod;
    }

    int gap = cnts[0]-cnts[1];
    while(gap--){
        val = (val*2)%mod;
    }

    string sv = to_string(val);
    int len_to_fill = max(0, (int)(5-sv.length()));
    while(len_to_fill--) cout << '0';
    cout << sv;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}