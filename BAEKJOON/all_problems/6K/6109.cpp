// 2025/01/15 11:30 ~ 11:46

// #include <bits/stdc++.h>
// using namespace std;

// void solve(){
//     int n, c; cin >> n >> c;

//     vector<vector<int>> dp(c+1, vector<int>(n+1));
//     for(int i=1; i<=c; ++i){
//         dp[i][0] = 1;

//         int k; cin >> k;
//         for(int j=k; j<=n; ++j){
//             dp[i][j] = dp[i-1][j]+dp[i][j-k];
//         }
//     }

//     cout << dp[c][n];
// }

// int main(void){
//     ios::sync_with_stdio(0);
//     cin.tie(0);
//     solve();
//     return 0;
// }


#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, c; cin >> n >> c;

    vector<int> dp(n+1);
    dp[0] = 1;

    for(int i=1; i<=c; ++i){
        int k; cin >> k;
        for(int j=k; j<=n; ++j) dp[j] += dp[j-k];
    }
    cout << dp[n];
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}