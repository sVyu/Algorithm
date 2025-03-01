#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int n; cin >> n;
    string s; cin >> s;
    int sz = s.size();

    int l=0, r=0;
    int ans = 1;
    int ex_cnt = 1;
    int cnts[26]={0,}; // cnts[n]
    cnts[s[r]-'a']++;

    while(r<sz){
        ++r;
        if(r>=sz) break;
        int tr = s[r]-'a'; // target right

        if(cnts[tr] == 0){
            ex_cnt++;
            while(ex_cnt > n){
                int tl = s[l]-'a';
                cnts[tl]--;
                if(cnts[tl] == 0) --ex_cnt;
                l++;
            }
        }
        ++cnts[tr];
        ans = max(ans, r-l+1);
    }

    cout << ans;   
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}