#include <bits/stdc++.h>
using namespace std;

int fp(vector<int>& parent, int v){
    if(parent[v] == v) return v;
    return parent[v] = fp(parent, parent[v]);
}

void up(vector<int>& parent, int a, int b){
    int pa = fp(parent, a);
    int pb = fp(parent, b);

    if(pa > pb) parent[pa] = pb;
    else        parent[pb] = pa;
}

void solve(){
    int case_num = 1;
    int n, m; cin >> n >> m;
    while(n){
        vector<int> parent(n+1, 0);
        for(int i=0; i<=n; i++) parent[i] = i;

        vector<bool> cycled(n+1, false);
        while(m--){
            int a, b; cin >> a >> b;
            if(fp(parent, a) != fp(parent, b)) up(parent, a, b);
            else{
                for(auto k:{a, b}) cycled[k] = true;
                up(parent, a, b);
            }
        }

        for(int i=1; i<=n; i++) fp(parent, i);
        vector<bool> removal(n+1, false);
        for(int i=1; i<=n; i++) if(cycled[i]) removal[parent[i]] = true;

        set<int> tp;
        for(auto p:parent) if(p and !removal[p]) tp.insert(p);

        cout << "Case " << case_num++ << ": ";
        int cnt = tp.size();
        if(cnt >= 2) cout << "A forest of " << cnt << " trees.\n";
        else if(cnt == 1) cout << "There is one tree.\n";
        else cout << "No trees.\n";

        cin >> n >> m;
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}