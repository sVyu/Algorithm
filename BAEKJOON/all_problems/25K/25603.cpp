// Âü°í : https://www.acmicpc.net/source/49286244

#include <bits/stdc++.h>
using namespace std;

const int mx = int(1e5)+7;
int s[mx], k, n;

bool check_pos(int num_limit){
    int not_pos_num_len = 0;
    for(int i=0; i<k; ++i){
        if(s[i] > num_limit) not_pos_num_len++;
        else not_pos_num_len = 0;

        if(not_pos_num_len >= n) return false;
    }
    return true;
}

void solve(){
    cin >> k >> n;
    for(int i=0; i<k; ++i) cin >> s[i];

    int l = 1, r = int(1e9);
    int ans = -1;
    while(l <= r){
        int mid = (l+r) >> 1;
        if(check_pos(mid)){
            ans = mid;
            r = mid-1;
        }
        else{
            l = mid+1;
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