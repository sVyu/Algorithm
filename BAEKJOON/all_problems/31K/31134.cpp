#include <iostream>
using namespace std;
typedef long long ll;

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    ll n;
    cin >> n;

    ll x;
    for(ll i=0; i<n; i++){
        cin >> x;
        cout << (2*x-1) << '\n';
    }
}