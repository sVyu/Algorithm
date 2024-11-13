#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, m; cin >> n >> m;
    int mx = int(1e9);
    vector<vector<int>> g(n+1, vector<int>(n+1, mx));
    vector<vector<int>> route(n+1, vector<int>(n+1, mx));

    while(m--){
        int a, b, val; cin >> a >> b >> val;
        if(g[a][b] > val){
            g[a][b] = val;
            g[b][a] = val;
            route[a][b] = b;
            route[b][a] = a;
        }
    }

    for(int k=1; k<=n; k++){
        for(int a=1; a<=n; a++){
            for(int b=1; b<=n; b++){
                if(g[a][b] > (g[a][k]+g[k][b])){
                    g[a][b] = g[a][k]+g[k][b];
                    route[a][b] = route[a][k];
                }
            }
        }
    }

    for(int x=1; x<=n; x++){
        for(int y=1; y<=n; y++){
            if(x==y) cout << '-';
            else cout << route[x][y];
            cout << ' ';
        }
        cout << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}