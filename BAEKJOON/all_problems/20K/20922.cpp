#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, k; cin >> n >> k;
    if(n == 1){
        cout << 1;
        return;
    }

    int sz = 1e5+1;
    int cnts[sz]={0};
    int l=0, r=0;

    int ns[n];  for(auto &n:ns) cin >> n;
    cnts[ns[0]]++;
    int ans = 1;

    while(r<n){
        if(cnts[ns[r]] > k){
            cnts[ns[l++]]--;
            continue;
        }

        if((r+1)<n){
            cnts[ns[++r]]++;
            if(cnts[ns[r]] <= k) ans = max(ans, r-l+1);
        } else {
            break;
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