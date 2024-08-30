#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

void solve(){
    int n; cin >> n;

    // negs, poss;
    vector<ll> negs;
    vector<ll> poss;
    bool has_zero=false;

    for(int i=0; i<n; i++){
        ll k; cin >> k;
        if(k<0)         negs.push_back(k);
        else if(k>0)    poss.push_back(k);
        else            has_zero=true;
    }

    sort(negs.begin(), negs.end(), greater<ll>());
    sort(poss.begin(), poss.end(), less<ll>());

    ll ans = 0;
    while(negs.size()>1){
        ll k2 = negs.back(); negs.pop_back();
        ll k1 = negs.back(); negs.pop_back();
        ans += k1*k2;
    }
    while(poss.size()>1){           //
        ll k2 = poss.back(); poss.pop_back();
        ll k1 = poss.back(); poss.pop_back();
        if(k1 == 1) ans += k1+k2;       // 3 mistakes
        else        ans += k1*k2;
    }

    if(negs.size() and !has_zero) ans += negs[0];
    if(poss.size()) ans += poss[0];

    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}

/*

if(k1 == 1) ans += k1+k2;       // 3 mistakes

1. k1 == 1 인 경우 처리 안함
2. k1 대신 k2로 판별
3. 1+3 등의 단순하게 2가 아닌 경우를 놓침

*/