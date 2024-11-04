#include <bits/stdc++.h>
using namespace std;

void cantor(int n){
    if(n == 0){
        cout << '-';
        return;
    }

    cantor(n-1);
    int sz = pow(3,n-1);
    for(int i=0; i<sz; i++) cout << ' ';
    cantor(n-1);
}

void solve(){
    int n;
    while(true){
        cin >> n;
        if(cin.eof()) break;

        cantor(n);
        cout << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}