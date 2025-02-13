#include <bits/stdc++.h>
using namespace std;

struct vi{
    int val;
    int index;

    bool operator < (const vi _vi) const {
        if(val != _vi.val) return val > _vi.val;
        else return index > _vi.index;
    }
};

void solve(){
    int n, l; cin >> n >> l;
    vector<int> zs(n); for(auto &z:zs) cin >> z;
    priority_queue<vi> pq;

    for(int i=0; i<n; ++i){
        pq.push({zs[i], i});
        while(!pq.empty() and pq.top().index <= (i-l)) pq.pop();
        cout << pq.top().val << ' ';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}