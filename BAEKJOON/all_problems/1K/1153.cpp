#include <bits/stdc++.h>
using namespace std;

const int mx = int(1e6)+1;
bool sv[mx]; // sieve

// Âü°í: °ñµå¹ÙÈåÀÇ ÃßÃø
void solve(){
    int n; cin >> n;
    if(n < 8){
        cout << -1;
        return;
    }

    fill(sv, sv+mx, true);
    for(int i=2; i<mx; ++i){
        if(sv[i]){
            for(int j=2*i; j<mx; j+=i){
                sv[j] = false;
            }
        }
    }

    vector<int> primes;
    for(int i=2; i<mx; ++i) if(sv[i]) primes.push_back(i);
    // cout << primes.size(); // 78498

    if(n%2){
        cout << 2 << ' ' << 3 << ' ';
        n -= 5;
    }else{
        cout << 2 << ' ' << 2 << ' ';
        n -= 4;
    }

    for(auto p:primes){
        if(sv[n-p]){
            cout << p << ' ' << n-p;
            return;
        }
    }

    // int l=0, r=primes.size()-1; // -1
    // while(l <= r){
    //     int val = primes[l]+primes[r];
    //     if(val == n){
    //         cout << primes[l] << ' ' << primes[r];
    //         return;
    //     }
    //     else if(val > n)    --r;
    //     else                ++l;
    // }

    // cout << -1;
    // return;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}