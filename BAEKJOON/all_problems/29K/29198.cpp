#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, m, k; cin >> n >> m >> k;
    vector<string> ss(n); for(auto &s:ss) cin >> s;

    for(auto &s:ss) sort(s.begin(), s.end());
    sort(ss.begin(), ss.end());

    vector<char> ans;
    for(int i=0; i<k; ++i){
        for(auto c:ss[i]){
            ans.push_back(c);
        }
    }

    sort(ans.begin(), ans.end());
    for(auto c:ans) cout << c;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}