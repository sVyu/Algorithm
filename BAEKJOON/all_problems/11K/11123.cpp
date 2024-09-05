// 2024.09.06 03:04 ~ 
#include <bits/stdc++.h>
using namespace std;

struct coord{
    int x;
    int y;
};

int dx[4]={0, 1, 0, -1};
int dy[4]={1, 0, -1, 0};

void solve(){
    int t; cin >>t;
    while(t--){
        int h, w; cin >> h >> w;
        vector<string> board(h, "");
        for(auto &r:board) cin >> r;

        bool visited[h][w];
        fill(&visited[0][0], &visited[0][0]+h*w, false);
        // fill(visited, visited+h, 1);

        int cnt = 0;
        for(int x=0; x<h; x++){
            for(int y=0; y<w; y++){
                if(board[x][y]=='#' and !visited[x][y]){
                    visited[x][y] = true;
                    cnt++;
                    queue<coord> q({{x,y}});
                    while(!q.empty()){
                        auto [x, y] = q.front(); q.pop();   //
                        for(int d=0; d<4; d++){
                            int nx=x+dx[d], ny=y+dy[d];
                            if(nx < 0 | nx >= h | ny < 0 | ny >= w) continue;
                            if(board[nx][ny] == '#' and !visited[nx][ny]){
                                visited[nx][ny]=true;
                                q.push({nx,ny});
                            }
                        }
                    }
                }
            }
        }
        cout << cnt << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}