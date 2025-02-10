#include <bits/stdc++.h>
using namespace std;

const int mx = int(2e6)+5;
vector<int> g[mx];
bool visited[mx];
int A[mx], B[mx];

bool dfs(int v){
    visited[v] = true;
    for(int u:g[v]){
        int bv = B[u];
        if(bv == -1 || (!visited[bv] and dfs(bv))){
            // A[v] = u;
            B[u] = v;
            return true;
        }
    }
    return false;
}

void solve(){
    int n, m; cin >> n >> m;

    for(int i=0; i<n; ++i){
        int k; cin >> k;
        while(k--){
            int num; cin >> num;
            g[i*2].push_back(num);
            g[i*2+1].push_back(num);
        }
    }

    fill(A, A+mx, -1);
    fill(B, B+mx, -1);

    int ans = 0;
    for(int i=0; i<(2*n); ++i){
        fill(visited, visited+mx, false);
        if(dfs(i)){
            ++ans;
            // if(ans == 4){
            //     for(int i=0; i<(2*n); ++i){
            //         cout << B[i] << ' ';
            //     }
            // }
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