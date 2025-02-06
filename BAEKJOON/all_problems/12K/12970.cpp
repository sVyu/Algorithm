#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, k; cin >> n >> k;
    
    int cnt_a = n/2;
    int cnt_b = n-cnt_a;

    if(k > cnt_a*cnt_b){
        cout << -1;
        return;
    }

    int quo = k / cnt_b;
    int mod = k % cnt_b;

    for(int i=0; i<quo; ++i,--n) cout << 'A';

    // for(int res=cnt_b; cnt_b>0; --cnt_b,--n){
    for(int res=cnt_b; res>0; --res, --n){
        if(res == mod){
            cout << 'A';
            --n;
        }
        cout << 'B';
    }

    for(int i=0; i<n; ++i) cout << 'A';
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}