#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll n; cin >> n;
    while(n){
        cout << ((n*(n+1)*(2*n+1)/6)+(n*(n+1)/2))/2 << '\n';
        cin >> n;
    }

    return 0;
}