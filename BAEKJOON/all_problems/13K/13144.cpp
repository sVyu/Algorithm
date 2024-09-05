#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll sum_cnt(ll a){
    ll sum = a*(a+1)/2;
    return sum;
}

void solve(){
    int n; cin >> n;
    ll zs[n]; for(auto &z:zs) cin >> z;

    int sz=1e5+1;
    int cnts[sz]{};
    cnts[zs[0]]++;
    ll ans=0;

    ll l=0, r=0, pre_r=-1;
    while(r<n){
        int nr = r+1;
        if(nr < n){
            if(cnts[zs[nr]]){
                ans += sum_cnt(r-l+1);
                ans -= sum_cnt(max(0LL, pre_r-l+1));  //
                while(zs[l] != zs[nr])  cnts[zs[l++]]--;
                cnts[zs[l++]]--;
                pre_r = r;
            }
            r = nr;
            cnts[zs[nr]]++;
        }else{
            break;
        }
    }

    ans += sum_cnt(r-l+1);
    ans -= sum_cnt(max(0LL, pre_r-l+1));
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}