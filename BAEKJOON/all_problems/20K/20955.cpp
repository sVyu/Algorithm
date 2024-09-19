#include <bits/stdc++.h>
using namespace std;

// find_parent
int fp(vector<int>& parent, int x){
    if(parent[x] == x) return x;
    return parent[x] = fp(parent, parent[x]);
}

// union_parent
void up(vector<int>& parent, int a, int b){
    int pa = fp(parent, a);
    int pb = fp(parent, b);

    if(pa>pb)   parent[pa]=pb;
    else        parent[pb]=pa;
}

void solve(){
    int n, m; cin >> n >> m;
    vector<int> parent(n+1, 0);
    for(int i=0; i<=n; i++) parent[i]=i;

    int ans = 0;
    while(m--){
        int u, v; cin >> u >> v;
        if(fp(parent, u) == fp(parent, v)) ans++;
        else up(parent, u, v);
    }
    for(int i=1; i<=n; i++) fp(parent, i);  //
    set<int> set_p;
    for(int i=1; i<=n; i++) set_p.insert(parent[i]);

    cout << ans+set_p.size()-1;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}