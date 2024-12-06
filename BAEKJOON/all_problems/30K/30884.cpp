#include <bits/stdc++.h>
using namespace std;

void solve(){
    string s; cin >> s;
    string ans = "";
    char pre = 'a';

    for(auto c:s){
        if(pre == ')' and c == '(')         ans += '+';
        else if(pre == '(' and c == ')')    ans += "1";

        ans += c;
        pre = c;
    }

    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}