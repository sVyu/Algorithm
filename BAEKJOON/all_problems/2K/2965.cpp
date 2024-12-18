#include <bits/stdc++.h>
using namespace std;

void solve(){
    int a, b, c;
    cin >> a >> b >> c;
    cout << max(b-a-1, c-b-1);
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}