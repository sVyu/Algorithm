#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, b; cin >> n >> b;

    string s = "";
    while(n>0){
        int k = n%b;
        if(k < 10)  s += to_string(k);
        else        s += 'A'+k-10;

        n /= b;
    }

    reverse(s.begin(), s.end());
    cout << s;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}