#include <bits/stdc++.h>
using namespace std;

int main(){
    string s; getline(cin, s);
    int n = s.length();

    string ans = "";
    ans += s[0];
    char pre = s[0];

    for(int i=1; i<n; ++i){
        if(pre == s[i]) continue;
        pre = s[i];
        ans += s[i];
    }

    cout << ans << '\n';
    return 0;
}