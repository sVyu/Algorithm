#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll cal_cnt(ll k, ll base){
    ll cnt = 0;
    while(k /= base) cnt += k;
    return cnt;
}

void solve(){
    ll n, m; cin >> n >> m;
    vector<ll> bases={2, 5};
    vector<ll> ncnts={0, 0};
    vector<ll> mcnts={0, 0};
    vector<ll> ocnts={0, 0};

    for(int i=0; i<bases.size(); i++){
        ll base = bases[i];
        ncnts[i] += cal_cnt(n, base);
        mcnts[i] += cal_cnt(m, base);
        ocnts[i] += cal_cnt(n-m, base);
    }

    cout << min(ncnts[0]-mcnts[0]-ocnts[0], ncnts[1]-mcnts[1]-ocnts[1]);
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}