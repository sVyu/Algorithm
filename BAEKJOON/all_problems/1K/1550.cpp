#include <bits/stdc++.h>
using namespace std;

void solve(){
    string s; cin >> s;
    int sz = s.size();

    int ans = 0;
    int val = 1;
    for(int i=sz-1; i>=0; --i){
        if(48 <= s[i] and s[i] <= 57)   ans += (s[i]-'0')*val;
        else                            ans += (s[i]-'A'+10)*val;
        val *= 16;
    }
    cout << ans;
}


int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}