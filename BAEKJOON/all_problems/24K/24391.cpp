#include <bits/stdc++.h>
using namespace std;

// find_parent
int fp(vector<int>& parent, int a){
    if(parent[a] == a) return a;
    return parent[a] = fp(parent, parent[a]);
}

// union_parent
void up(vector<int>& parent, int a, int b){
    int pa = fp(parent, a);
    int pb = fp(parent, b);

    if(pa > pb) parent[pa] = pb;
    else        parent[pb] = pa;
}

void solve(){
    int n, m; cin >> n >> m;
    vector<int> parent(n+1, 0);
    for(int i=0; i<=n; ++i) parent[i]=i;

    while(m--){
        int a, b; cin >> a >> b;
        if(fp(parent, a) != fp(parent, b)) up(parent, a, b);
    }
    for(int i=0; i<=n; ++i) fp(parent, i);

    vector<int> schs(n, 0); for(auto &s:schs) cin >> s;
    int now = parent[schs[0]];
    int ans = 0;

    for(int i=1; i<n; ++i){
        if(now != fp(parent, schs[i])){
            now = parent[schs[i]];
            ++ans;
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