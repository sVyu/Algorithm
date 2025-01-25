#include <bits/stdc++.h>
using namespace std;

void solve(){
    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        vector<string> ss1(n); for(auto &s:ss1) cin >> s;
        vector<string> ss2(n); for(auto &s:ss2) cin >> s;

        sort(ss1.begin(), ss1.end());
        sort(ss2.begin(), ss2.end());

        bool same = true;
        for(int i=0; i<n; ++i){
            if(ss1[i] != ss2[i]){
                same = false;
                break;
            }
        }

        string ans = same ? "NOT CHEATER\n" : "CHEATER\n";
        cout << ans;
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}