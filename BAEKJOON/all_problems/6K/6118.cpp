#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, m; cin >> n >> m;
    vector<vector<int>> g(n+1);
    while(m--){
        int a, b; cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }

    queue<int> q({1});
    vector<bool> visited(n+1, false);
    visited[1] = true;

    int dist = 0;
    int min_u = 1, cnt = 0;
    while(!q.empty()){
        int q_size = q.size();
        bool flag = true;

        while(q_size--){
            int v = q.front(); q.pop();
            for(auto u:g[v]){
                if(!visited[u]){
                    if(flag){
                        flag = false;
                        min_u = 3e4, cnt = 0;
                    }
                    visited[u] = true;
                    q.push(u);
                    min_u = min(min_u, u);
                    cnt++;
                }
            }
        }
        if(flag) break;
        dist++;
    }
    cout << min_u << ' ' << dist << ' ' << cnt;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}