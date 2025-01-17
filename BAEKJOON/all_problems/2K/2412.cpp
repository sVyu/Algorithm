// 2025/01/17 11:40 ~ 12:08
#include <bits/stdc++.h>
using namespace std;

struct dot{
    int x;
    int y;
};

void solve(){
    int n, t; cin >> n >> t;

    map<int, set<int>> grvs, visited; // groove : Ȩ
    for(int i=0; i<n; ++i){
        int x, y; cin >> x >> y;
        grvs[x].insert(y);
    }

    queue<dot> q({{0, 0}});
    int round = 0;
    while(!q.empty()){
        ++round;
        int sz = q.size();
        while(sz--){
            auto [x, y] = q.front(); q.pop();
            for(int px=-2; px<=2; px++){
                for(int py=-2; py<=2; py++){
                    int nx = x+px, ny = y+py;
                    if(grvs[nx].count(ny) and !visited[nx].count(ny)){
                        if(ny == t){
                            cout << round;
                            return;
                        }
                        visited[nx].insert(ny);
                        q.push({nx, ny});
                    }
                }
            }
        }
    }

    cout << -1;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}