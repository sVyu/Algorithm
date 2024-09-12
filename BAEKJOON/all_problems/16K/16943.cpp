#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    string a; cin >> a;
    ll b; cin >> b;
    sort(a.begin(), a.end());

    ll ans = -1;
    do{
        if(a[0] == '0') continue;
        ll lla = stoll(a);
        if(lla < b) ans = max(ans, lla);
    }while(next_permutation(a.begin(), a.end()));
    cout << ans;
}

int main(void){
    ios::sync_with_stdio;
    cin.tie(0);
    solve();
    return 0;
}