#include <bits/stdc++.h>
using namespace std;

int cal(vector<int> const &zs){
    // 카드들 XOR 연산
    int val = zs[0];
    for(auto z:vector<int>(zs.begin()+1, zs.end())){
        val ^= z; // XOR
    }

    // 1의 개수만큼 점수 획득
    int cnt = 0;
    while(val > 0){
        cnt += val%2;
        val /= 2;
    }
    return cnt;
}

void solve(){
    int n; cin >> n;
    vector<int> zs(n); for(auto &z:zs) cin >> z;
    zs.insert(zs.begin(), 0);
    vector<int> dp(n+1, -1);
    dp[0] = 0;

    for(int i=2; i<=n; ++i){
        // cal vector (i-1) ~ i
        if(dp[i-2] != -1) dp[i] = max(dp[i], dp[i-2] + cal(vector<int>(zs.begin()+(i-1), zs.begin()+(i+1))));

        // cal vector (i-2) ~ i
        if(i < 3) continue;
        if(dp[i-3] != -1) dp[i] = max(dp[i], dp[i-3] + cal(vector<int>(zs.begin()+(i-2), zs.begin()+(i+1))));
    }

    int ans = (dp[n] != -1) ? dp[n] : 0;
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}