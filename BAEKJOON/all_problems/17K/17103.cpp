#include <bits/stdc++.h>
using namespace std;

const int sz=1e6+1;
bool sieve[sz];

void solve(){
    fill(sieve, sieve+sz, true);
    vector<int> primes{};
    for(int i=2; i<sz; i++){
        if(sieve[i]){
            primes.push_back(i);
            for(int j=2*i; j<sz; j+=i){
                sieve[j] = false;
            }
        }
    }

    int len_primes = primes.size();
    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        int l=0, r=len_primes-1;
        int ans=0;
        while(l<=r){
            int val=primes[l]+primes[r];
            if(val < n) l++;
            else if(val > n) r--;
            else{
                ans++;
                l++;
                r--;
            }
        }
        cout << ans << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}