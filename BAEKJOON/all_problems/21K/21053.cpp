#include <iostream>
#include <vector>
using namespace std;
// typedef long long ll;

int solve(){
    int n; cin >> n;
    vector<int> rs(n);
    for(int i=0; i<n; i++) cin >> rs[i];

    int mod = 1e9 + 7;
    int cnt_one = 0, cnt_setlits = 0;
    int ans = 0;

    for(auto r:rs){
        if(r == 1){
            cnt_one += 1;
        }else if(r == 2){
            cnt_setlits = (cnt_setlits*2 + cnt_one)%mod;
        }else{
            ans = (ans + cnt_setlits)%mod;
        }
    }

    cout << ans;
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}