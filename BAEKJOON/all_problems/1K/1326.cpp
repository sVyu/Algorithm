#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    vector<int> zs(n); for(auto &z:zs) cin >> z;

    int a, b; cin >> a >> b;
    --a; --b;
    if(a == b){
        cout << 0;
        return;
    }

    vector<bool> visited(n, false);
    visited[a] = true;

    queue<int> q({a});
    int cnt = 1;

    while(!q.empty()){
        int q_sz = q.size();
        while(q_sz--){
            int v = q.front(); q.pop();
            for(int mul = 1; mul < 100000; ++mul){
                int nv = v+mul*zs[v];
                if(nv >= n) break;
                if(nv == b){
                    cout << cnt;
                    return;
                }

                if(visited[nv]) continue;
                visited[nv] = true;
                q.push(nv);
            }

            for(int mul = 1; mul < 100000; ++mul){
                int nv = v-mul*zs[v];
                if(nv < 0) break;
                if(nv == b){
                    cout << cnt;
                    return;
                }

                if(visited[nv]) continue;
                visited[nv] = true;
                q.push(nv);
            }
        }
        ++cnt;
    }
    cout << -1;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}