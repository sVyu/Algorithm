#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int t; cin >> t;
    int mx1 = int(5e4)+1;
    vector<bool> seive(mx1, true);

    vector<ll> primes; //
    for(int i=2; i<mx1; ++i){
        if(seive[i])
            primes.push_back(i);
            for(int j=2*i; j<mx1; j+=i) seive[j] = false;
    }

    int primes_sz = primes.size();
    // cout << primes_sz;
    ll mx2 = 150000;
    vector<ll> ans(mx2, -1);

    for(int i=0; i<(primes_sz-1); ++i){
        for(int j=i+1; j<primes_sz; ++j){
            ll val = primes[i]*primes[j]; // ll, int
            if(val >= mx2) break;
            ans[val] = val;
        }
    }

    for(int i=int(mx2-2); i>=0; --i){ // ++i -> --i, mx2..
        if(ans[i] == -1) ans[i] = ans[i+1];
    }

    while(t--){
        int k; cin >> k;
        cout << ans[k] << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}