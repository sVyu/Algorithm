#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    vector<int> zs(n); for(auto &z:zs) cin >> z;

    // main logic
    int ans = 1;
    for(bool flag:{true, false}){
        int pre = zs[0];
        int cnt = 1;

        for(int z:zs){
            if(pre == z) continue;
            if(pre < z){
                if(flag){
                    pre = z;
                    ++cnt;
                    flag = !flag; // flag != flag;
                }else{
                    pre = z;
                }
            }
            else if(pre > z){
                if(!flag){
                    pre = z;
                    ++cnt;
                    flag = !flag;
                }else{
                    pre = z;
                }
            }
        }
        ans = max(ans, cnt);
    }
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}