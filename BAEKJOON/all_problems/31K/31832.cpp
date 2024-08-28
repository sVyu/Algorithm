#include <bits/stdc++.h>
using namespace std;

int solve(){
    int n; cin >> n;

    while(n--){
        string s; cin >> s;

        if(s.length() > 10) continue;
        int upper=0, lower=0;
        for(auto c:s){
            if(c-'a' >= 0 and c-'z' <= 0)       lower++;
            else if(c-'A' >= 0 and c-'Z' <= 0)  upper++;
        }
        if(upper > lower) continue;

        bool find = false;
        for(auto c:s){
            if(!(c-'0' >= 0 and c-'9' <= 0)) find = true;
        }
        if(!find) continue;

        cout << s;
        return 0;
    }
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}