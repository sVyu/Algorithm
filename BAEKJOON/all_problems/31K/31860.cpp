#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, m, k; cin >> n >> m >> k;

    priority_queue<int, vector<int>, less<int>> pq;
    for(int i=0; i<n; i++){
        int d; cin >> d;
        pq.push(d);
    }

    int pre = 0;
    vector<int> ans;

    while(!pq.empty()){
        int d = pq.top(); pq.pop();

        int val = pre/2 + d;
        ans.push_back(val);
        pre = val;

        d -= m;
        if(d > k) pq.push(d);
    }

    cout << ans.size() << '\n';
    for(auto a:ans) cout << a << '\n';
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}