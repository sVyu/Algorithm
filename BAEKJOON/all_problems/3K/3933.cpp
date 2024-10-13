#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    const int sz = pow(2, 15);
    vector<vector<int>> dp(sz+1, vector<int>(5, 0));
    dp[0][0] = 1;

    int limit = int(sqrt(sz));
    for(int k=1; k<=limit; k++){
        int val = k*k;
        for(int i=val; i<=sz; i++){
            for(int j=1; j<=4; j++){
                dp[i][j] += dp[i-val][j-1];
            }
        }
    }

    int n; cin >> n;
    while(n){
        int cnt = accumulate(dp[n].begin(), dp[n].end(), 0);
        cout << cnt << '\n';
        cin >> n;
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}