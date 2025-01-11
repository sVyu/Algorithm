#include <bits/stdc++.h>
using namespace std;

void solve(){
    string a, b, c, d; cin >> a >> b >> c >> d;
    cout << stoll(a+b)+stoll(c+d);
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}