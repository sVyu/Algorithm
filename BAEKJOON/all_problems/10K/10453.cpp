#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int t; cin >> t;
    while(t--){
        string s1, s2; cin >> s1 >> s2;
        int cnt_b[2]={0};
        for(auto c:s1) if(c=='b') cnt_b[0]++;
        for(auto c:s2) if(c=='b') cnt_b[1]++;

        if((s1.size() != s2.size()) || (cnt_b[0] != cnt_b[1])){
            cout << -1 << '\n';
            continue;
        }

        int n = cnt_b[0];
        int s1_idxs_b[n]={0}, s2_idxs_b[n]={0};
        int idx1=0, idx2=0;

        int len_s = s1.size();
        for(int i=0; i<len_s; i++){
            if(s1[i] == 'b') s1_idxs_b[idx1++] = i;
            if(s2[i] == 'b') s2_idxs_b[idx2++] = i;
        }

        ll ans = 0;
        for(int i=0; i<n; i++){
            ans += abs(s1_idxs_b[i]-s2_idxs_b[i]);
        }
        cout << ans << '\n';
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}