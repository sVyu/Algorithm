#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    vector<int> zs(n,0);
    for(auto &z:zs) cin >> z;
    sort(zs.begin(), zs.end());

    int ans = INT_MAX;
    for(int i=0; i<n-3; i++){
        for(int j=i+3; j<n; j++){
            int target = zs[i]+zs[j];
            int l=i+1, r=j-1;

            while(l<r){
                int now=zs[l]+zs[r];
                ans = min(ans, abs(target-now));
                if(now < target)    l++;        //
                else                r--;
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