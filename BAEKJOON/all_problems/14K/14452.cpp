#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, tmax; cin >> n >> tmax; // cin >> n, tmax;
    vector<int> zs(n); for(auto &z:zs) cin >> z;

    int lo = 1, hi = n; // hi = int(1e4) -> n
    int ans = n;

    while(lo <= hi){
        int mid = (lo+hi)/2;        // mid == tmp_k

        priority_queue<int, vector<int>, greater<int>> pq; // queue -> priority_queue
        // priority_queue<int, vector<int>, greater<int>> tpq = pq;
        int i = 0;
        for(i=0; i<mid; ++i) pq.push(zs[i]);

        for(int t=1; t<=tmax; ++t){
            while(!pq.empty() and t == pq.top()){ // !pq.empty()
                pq.pop();
                if(i<n) pq.push(t+zs[i++]);
            }
        }

        if(i >= n and pq.empty()){
            ans = mid;
            hi = mid-1;
        }else{
            lo = mid+1;
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