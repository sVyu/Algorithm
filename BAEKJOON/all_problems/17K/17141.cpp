// 2024.09.17. 12:25
#include <bits/stdc++.h>
using namespace std;

struct pt{
    int x;
    int y;
    int t;
};

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

void solve(){
    int n, m; cin >> n >> m;
    vector<vector<int>> board(n, vector<int>(n, -1));
    for(auto &r: board) for(auto &c:r) cin >> c;

    vector<pt> pts;
    for(int x=0; x<n; x++){
        for(int y=0; y<n; y++){
            if(board[x][y] == 2) pts.push_back({x, y, 0});
        }
    }

    int pts_sz = pts.size();
    vector<int> zeros(pts_sz, 0);
    for(int i=0; i<m; i++) zeros[pts_sz-1-i]=1;

    int mx = 3e4;
    int ans = mx;
    do{
        queue<pt> q;
        bool visited[n][n];
        fill(&visited[0][0], &visited[0][0]+n*n, false);

        for(int i=0; i<pts_sz; i++){
            if(zeros[i]){
                q.push(pts[i]);
                auto [x, y, t] = pts[i];
                visited[x][y] = true;
            }
        }

        int time=0;
        while(!q.empty()){
            auto [x, y, t] = q.front(); q.pop();
            for(int d=0; d<4; d++){
                int nx=x+dx[d], ny=y+dy[d];
                if(nx < 0 | nx >= n | ny < 0 | ny >= n) continue;
                if(board[nx][ny] == 1) continue;
                if(!visited[nx][ny]){
                    visited[nx][ny] = true;
                    q.push({nx, ny, t+1});
                    time = max(time, t+1);
                }
            }
        }

        bool pos = true;
        for(int x=0; x<n; x++){
            for(int y=0; y<n; y++){
                if(board[x][y] == 1) continue;
                if(!visited[x][y]) pos=false;
            }
        }
        if(pos) ans = min(ans, time);

    }while(next_permutation(zeros.begin(), zeros.end()));

    if(ans==mx) ans=-1;
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}