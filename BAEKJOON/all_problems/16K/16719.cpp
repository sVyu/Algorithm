#include <bits/stdc++.h>
using namespace std;

void btr(string s, bool visited[], int sz, int cnt){
    string ans;
    for(int i=0; i<cnt; ++i) ans += 'a'; // t -> "aaa.."
    int ti=-1;

    if(cnt > 1) btr(s, visited, sz, cnt-1);

    for(int i=0; i<sz; ++i){
        if(visited[i]) continue;

        string tmp;
        for(int j=0; j<sz; ++j){
            if(visited[j] || i==j) tmp += s[j];
        }

        if(ans.compare(tmp) > 0){
            ans = tmp;
            ti = i;
        }
    }

    cout << ans << '\n';
    visited[ti] = true;
}

void solve(){
    string s; cin >> s;
    int sz = s.size();
    bool visited[sz] = {false, };

    btr(s, visited, sz, sz);
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}