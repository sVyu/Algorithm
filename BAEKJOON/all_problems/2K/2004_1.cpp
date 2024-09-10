#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll cal_cnt(ll &k, ll base){
    ll val=1, cnt=0;
    while(k >= val){
        val *= base;
        cnt = cnt*base+1;
    }
    k -= val/base;
    return cnt/base;
}

void solve(){
    ll n, m; cin >> n >> m;
    vector<ll> bases={2, 5};
    vector<ll> ncnts={0, 0};
    vector<ll> mcnts={0, 0};
    vector<ll> ocnts={0, 0};

    for(int i=0; i<bases.size(); i++){
        ll tmpn = n, tmpm = m, tmpo = n-m;
        ll base = bases[i];
        while(tmpn >= base) ncnts[i] += cal_cnt(tmpn, base);
        while(tmpm >= base) mcnts[i] += cal_cnt(tmpm, base);
        while(tmpo >= base) ocnts[i] += cal_cnt(tmpo, base);
    }

    cout << min(ncnts[0]-mcnts[0]-ocnts[0], ncnts[1]-mcnts[1]-ocnts[1]);
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}