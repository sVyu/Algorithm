#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    string s; cin >> s;
    reverse(s.begin(), s.end());
    s.pop_back();

    int ans=0;
    bool has_met_one = false;
    for(char c:s){
        if(c == '1'){
            if(!has_met_one){
                ans = 1;
                has_met_one = true;
            }
        }
        else{
            if(has_met_one) ++ans;
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