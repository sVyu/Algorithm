#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    ll n, k; cin >> n >> k;

    ll lo=0, hi=n-(n/2+n%2);
    while(lo <= hi){
        ll mid = (lo+hi)/2;
        ll val = (mid+1)*(n-mid+1);

        if(val == k){
            cout << "YES";
            return;
        }else if(val > k)   hi=mid-1;
        else                lo=mid+1;
    }

    cout << "NO";
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}