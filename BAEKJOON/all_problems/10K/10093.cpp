#include <iostream>
using namespace std;
typedef long long ll;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll a, b;
    cin >> a >> b;
    if(a > b) swap(a, b);

    cout << max(b-1-a, (ll)0) << '\n';
    for(ll n = (a+1); n < b; n++){
        cout << n << ' ';
    }

    return 0;
}