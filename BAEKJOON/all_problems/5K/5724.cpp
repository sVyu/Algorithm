#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(void){
    int n; cin >> n;
    while(n){
        ll ans = 0;
        for(int k=1; k<=n; k++){
            ans += k*k;
        }
        cout << ans << '\n';
        cin >> n;
    }
    return 0;
}