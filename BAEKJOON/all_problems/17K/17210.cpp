#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(void){
    ll n; cin >> n;
    int val; cin >> val;

    if(n >= 6){
        cout << "Love is open door";
        return 0;
    }

    for(int i=2; i<=n; ++i){
        cout << (val+i+1)%2 <<'\n';
    }
    return 0;
}