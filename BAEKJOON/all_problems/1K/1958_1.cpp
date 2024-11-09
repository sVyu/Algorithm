// WA
#include <bits/stdc++.h>
using namespace std;

vector<int> cal_lcs(string s1, string s2){
    int n1 = s1.size(), n2 = s2.size();
    vector<int> dp(n1, 0);

    for(int i=0; i<n2; i++){
        int cnt = 0;
        for(int j=0; j<n1; j++){
            if(cnt < dp[j]) cnt = dp[j];
            else if(s2[i] == s1[j]) dp[j] = cnt+1;
        }
    }

    return dp;
}

void solve(){
    string s1, s2, s3; cin >> s1 >> s2 >> s3;
    vector<int> lcs1 = cal_lcs(s1, s2);

    string new_s;
    int sz = s1.size();
    for(int i=0; i<sz; i++) if(lcs1[i]) new_s += s1[i];

    vector<int> lcs2 = cal_lcs(new_s, s3);
    int ans = *max_element(lcs2.begin(), lcs2.end());
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}