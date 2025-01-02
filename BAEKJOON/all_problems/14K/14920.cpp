#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    int round = 1;

    while(n != 1){
        if(n%2 == 0)    n/=2;
        else            n = 3*n+1;
        ++round;
    }
    cout << round;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}