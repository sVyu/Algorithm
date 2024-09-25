#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int n, m; cin >> n >> m;
    priority_queue<ll, vector<ll>, greater<ll>> pq;

    while(n--){
        ll k; cin >> k;
        pq.push(k);
    }

    while(m--){
        ll a = pq.top(); pq.pop();
        ll b = pq.top(); pq.pop();
        for(int i=0; i<2; i++) pq.push(a+b);
    }

    ll ans=0;
    while(!pq.empty()){
        ans += pq.top(); pq.pop();
    }
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}