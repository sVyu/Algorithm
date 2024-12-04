#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct e{
    int v;
    ll d;
};

void dfs(int p, int v, vector<vector<e>>& g, vector<int>& depths, vector<e>& parents){
    for(auto [u, d]:g[v]){
        if(u == p) continue; // p: parent
        depths[u] = depths[v]+1;
        parents[u] = {v, d};
        dfs(v, u, g, depths, parents);
    }
}

e up(vector<vector<e>>&st, int v, int gap){
    ll d = 0;
    int lg_gap = int(log2(gap));
    for(int i=lg_gap; i>=0; i--){
        if((1 << i) & gap){
            d += st[i][v].d;
            v = st[i][v].v;
        }
    }
    return {v, d};
}

void solve(){
    int n; cin >> n;
    int mx = n+1;

    vector<vector<e>> g(mx);
    vector<int> depths(mx, 0);
    vector<e> parents(mx);

    for(int i=1; i<n; i++){
        int v, u, d; cin >> v >> u >> d;
        g[v].push_back({u, d});
        g[u].push_back({v, d});
    }
    dfs(-1, 1, g, depths, parents);

    int k = int(log2(*max_element(depths.begin(), depths.end())));
    vector<vector<e>> st(k+1, vector<e>(mx, {-1, -1}));
    for(int j=1; j<=n; j++) st[0][j] = parents[j];
    for(int i=1; i<=k; i++){
        for(int j=1; j<=n; j++){
            auto [tv, td] = st[i-1][j];
            if(st[i-1][tv].v <= 0) continue;
            st[i][j] = {st[i-1][tv].v, st[i-1][tv].d + td};
        }
    }

    // for(auto r:st){
    //     for(auto [v, d]:r) cout << "(" << v << ", " << d << ")";
    //     cout << '\n';
    // }

    int m; cin >> m;
    while(m--){
        int a, b; cin >> a >> b;
        ll ans = 0;

        if(depths[a] > depths[b]) swap(a, b);
        if(depths[a] < depths[b]){
            auto [tv, td] = up(st, b, depths[b]-depths[a]);
            b = tv;
            ans = td;
        }

        if(a != b){
            for(int i=int(log2(depths[a])); i>=0; i--){
                if(st[i][a].v != st[i][b].v){
                    ans += st[i][a].d + st[i][b].d;
                    a = st[i][a].v;
                    b = st[i][b].v;
                }
            }
            ans += st[0][a].d + st[0][b].d;
        }

        cout << ans << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}