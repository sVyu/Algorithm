// AC
#include <bits/stdc++.h>
using namespace std;

void solve(){
    string s1, s2, s3; cin >> s1 >> s2 >> s3;
    s1 = "_"+s1;
    s2 = "_"+s2;
    s3 = "_"+s3;

    int n1 = s1.size(), n2 = s2.size(), n3 = s3.size();
    int dp[n1][n2][n3];
    fill(&dp[0][0][0], &dp[0][0][0]+n1*n2*n3, 0);

    int ans = 0;
    for(int i=1; i<n1; i++){
        for(int j=1; j<n2; j++){
            for(int k=1; k<n3; k++){
                if(s1[i] == s2[j] and s1[i] == s3[k])
                    dp[i][j][k] = dp[i-1][j-1][k-1]+1;
                else
                    dp[i][j][k] = max(max(dp[i-1][j][k], dp[i][j-1][k]), dp[i][j][k-1]);
                ans = max(ans, dp[i][j][k]);
            }
        }
    }

    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}