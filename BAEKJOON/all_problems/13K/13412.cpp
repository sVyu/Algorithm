#include <bits/stdc++.h>
using namespace std;

int gcd(int a, int b){
    if(b==0) return a;
    return gcd(b, a%b);
}

void solve(){
    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        int sqrt_n = int(sqrt(n));
        int cnt = 0;

        for(int i=1; i<=sqrt_n; i++){
            if(n%i == 0){
                if(gcd(i, n/i) == 1) cnt++;
            }
        }
        cout << cnt << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}