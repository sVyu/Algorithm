#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    ll n; cin >> n;

    ll sqrt_n = (ll)sqrt(n);
    ll sqrt_n_plus_2 = (ll)sqrt(n+2);

    for(ll a=1; a<=sqrt_n; a++){
        ll c=n/a;
        if(a*c == n){
            for(ll b=1; b<=sqrt_n_plus_2; b++){
                if((n+2)%b == 0){
                    ll d = ((n+2)/b);
                    if(a*c == n and (-b)*c+a*d == (n+1) and b*d == (n+2)){
                        cout << a << ' ' << -b << ' ' << c << ' ' << d;
                        return;
                    }
                    if(a*c == n and b*c+a*(-d) == (n+1) and b*d == (n+2)){
                        cout << a << ' ' << b << ' ' << c << ' ' << -d;
                        return;
                    }
                }
            }
        }
    }
    cout << -1;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}