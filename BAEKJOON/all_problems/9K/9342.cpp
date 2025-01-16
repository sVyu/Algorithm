#include <bits/stdc++.h>
// #include <regex>
using namespace std;

void solve(){
    int t; cin >> t;
    while(t--){
        string s; cin >> s;
        regex re("^[A-F]?A+F+C+[A-F]?");

        string ans = regex_match(s,re) ? "Infected!\n" : "Good\n";
        cout << ans;
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}