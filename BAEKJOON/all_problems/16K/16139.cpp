#include <bits/stdc++.h>
using namespace std;

void solve(){
    string s; cin >> s;
    int sz = s.length();

    vector<vector<int>> cnts(26, vector<int>(sz+1, 0));
    for(int j=1; j<=sz; j++) cnts[s[j-1]-'a'][j] = 1;
    for(int i=0; i<26; i++){
        for(int j=1; j<=sz; j++) cnts[i][j] += cnts[i][j-1];
    }

    int q; cin >> q;
    while(q--){
        char c; int l, r; cin >> c >> l >> r;
        cout << cnts[c-'a'][r+1]-cnts[c-'a'][l] << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}