#include <bits/stdc++.h>
using namespace std;

void solve(){
    int t; cin >> t;
    while(t--){
        int q, k; cin >> q >> k;
        priority_queue<int, vector<int>, greater<int>> pq;
        int insert_cnt=0, ans=0;

        while(q--){
            string cmd; cin >> cmd;
            if(cmd == "insert"){
                int val; cin >> val;

                if(insert_cnt++ < k){
                    pq.push(val);
                    ans ^= val;
                }else{
                    if(val > pq.top()){
                        pq.push(val);
                        ans ^= pq.top(); pq.pop();
                        ans ^= val;
                    }
                }
            }
            else cout << ans << '\n';
        }
    }
}

int main(void){
    ios::sync_with_stdio;
    cin.tie(0);
    solve();
    return 0;
}