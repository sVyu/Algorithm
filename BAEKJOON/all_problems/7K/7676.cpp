#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int range, n;
    cin >> range >> n;

    while(range != -1 and n != -1){
        int l, mid;
        l = mid = -1001;
        int ans = 0;

        vector<int> zs(n); for(auto &z:zs) cin >> z;
        sort(zs.begin(), zs.end());

        for(auto z:zs){
            if((l+range) >= z){
                mid = z;
            }
            else if((mid+range) >= z){
                continue;
            }
            else{
                l=z;
                ans++;
            }
        }

        cout << ans << '\n';
        cin >> range >> n;
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}