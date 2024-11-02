#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    ll x, y; cin >> x >> y;

    for(int day=0; day<=y; day++){
        ll mid = day/2;
        ll val = mid*(mid+1);
        if(day%2) val += (mid+1);

        if(val >= (y-x)){
            cout << day;
            return;
        }
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}