#include <bits/stdc++.h>
using namespace std;

struct dcnt{
    int d;
    int cnt;
};

// pq cmp는 반대로 해야한다
struct cmp{
    bool operator()(dcnt a, dcnt b){
        if(a.d != b.d) return a.d < b.d;    // return
        return a.cnt < b.cnt;
    }
};

void solve(){
    int n; cin >> n;
    priority_queue<dcnt, vector<dcnt>, cmp> pq;
    priority_queue<int, vector<int>, less<int>> pre_cnts;
    for(int i=0; i<n; i++){
        int d, cnt; cin >> d >> cnt;
        pq.push({d, cnt});
    }

    int ans=0;
    for(int t=n; t>=1; t--){
        while(!pq.empty() and t <= pq.top().d){
            pre_cnts.push(pq.top().cnt);
            pq.pop();
        }

        if(pre_cnts.empty()) continue;
        ans += pre_cnts.top();
        pre_cnts.pop();
    }

    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}