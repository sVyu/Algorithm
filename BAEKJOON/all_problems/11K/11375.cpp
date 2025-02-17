// 20250209 17:22 ~ 17:28
#include <bits/stdc++.h>
using namespace std;

const int mx = 1001;
vector<int> g[mx];
bool visited[mx];
int A[mx], B[mx];

bool dfs(int v){
    visited[v] = true;
    for(int u:g[v]){
        int bv = B[u];
        if(bv == -1 || (!visited[bv] and dfs(bv))){
            A[v] = u;
            B[u] = v;
            return true;
        }
    }
    return false;
}

void solve(){
    int n, m; cin >> n >> m;
    for(int i=0; i<n; ++i){
        int cnt; cin >> cnt;
        while(cnt--){
            int k; cin >> k;
            g[i].push_back(k);
        }
    }

    fill(A, A+mx, -1); // init_value: false -> -1
    fill(B, B+mx, -1); // init_value: false -> -1

    int ans = 0;
    for(int i=0; i<n; ++i){
        fill(visited, visited+mx, false);
        if(dfs(i)) ++ans;
    }

    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}