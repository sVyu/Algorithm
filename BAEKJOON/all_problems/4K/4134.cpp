#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

bool check_prime(ll a){
    if(a == 1)          return false;
    else if(a == 2)     return true;
    else if(a % 2 == 0) return false;
    else{
        ll target = ll(sqrt(a));
        for(ll k=3; k<=target; k+=2){
            if(a%k == 0) return false;
        }
        return true;
    }
}

void solve(){
    int t; cin >> t;
    while(t--){
        ll n; cin >> n;
        while(!check_prime(n)){
            ++n;
        }
        cout << n << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}