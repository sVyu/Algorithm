// 2024.09.04. 18:01~18:31
// segfault(out of bounds), 틀렸습니다(부동 소수점 오차)
#include <bits/stdc++.h>
using namespace std;

// probabilitys
const int sz = 5e5+1;     // 5e+1??
double ps[sz]={0.0, 1.0}; //
vector<vector<int>> g(sz, vector<int>());

void init_p(int parent, int v){
    int num_child = g[v].size()-1;  //

    for(auto u:g[v]){
        if(u == parent) continue;   //
        ps[u] = ps[v]/num_child;
        init_p(v, u);
    }
    if(num_child) ps[v]=0;
}

void solve(){
    int n, w; cin >> n >> w;
    for(int i=0; i<n-1; i++){
        int u, v; cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    g[1].push_back(0);

    init_p(0, 1);
    int num_pp = 0;             // positive probability
    double sum_pp = 0;
    for(int v=1; v<=n; v++){
        if(ps[v] > 0){
            num_pp++;
            sum_pp += ps[v];
        }
    }

    cout.precision(10);         //
    cout << sum_pp*w/num_pp;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}