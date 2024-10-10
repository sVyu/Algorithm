#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int parent[1001];

struct e{
    int v;
    int u;
    int val;

    bool operator < (const e _e) const{
        if(val != _e.val)   return val > _e.val;    //
        else if(v != _e.v)  return v > _e.v;
        else                return u > _e.u;
    };
};

int fp(int a){
    if(a == parent[a]) return a;
    return parent[a] = fp(parent[a]);
}

void up(int a, int b){
    int pa = fp(a);
    int pb = fp(b);

    if(pa < pb) parent[pa] = pb;
    else        parent[pb] = pa;
}

void solve(){
    for(int i=1; i<1001; i++) parent[i]=i;

    int n; cin >> n;
    priority_queue<e> pq;

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            int c; cin >> c;
            if(i==j) continue;
            pq.push({i, j, c});
        }
    }

    ll ans = 0;
    while(!pq.empty()){
        auto [v, u, c] = pq.top(); pq.pop();
        if(fp(v) != fp(u)){
            up(v, u);
            ans += c;
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