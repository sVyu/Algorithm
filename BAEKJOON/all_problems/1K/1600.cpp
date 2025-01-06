#include <bits/stdc++.h>
using namespace std;

struct dot{
    int jump_cnt;
    int x;
    int y;
};

int inc_x[4] = {0, 1, 0, -1};
int inc_y[4] = {1, 0, -1, 0};

int inc_hx[8] = {-2, -1, 1, 2, 2, 1, -1, -2};
int inc_hy[8] = {1, 2, 2, 1, -1, -2, -2, -1};

void solve(){
    int k, w, h; cin >> k >> w >> h;
    if(w == 1 and h == 1){
        cout << 0;
        return;
    }

    int board[h][w]; for(auto &r:board) for(auto &el:r) cin >> el;
    int visited[h][w];
    for(int x=0; x<h; ++x){
        for(int y=0; y<w; ++y){
            visited[x][y] = INT_MAX;
        }
    }
    visited[0][0] = true;

    int move_cnt = 0;
    queue<dot> q({{0, 0, 0}});
    while(!q.empty()){
        ++move_cnt;
        int sz = q.size();
        while(sz--){
            auto [jump_cnt, x, y] = q.front(); q.pop();

            // monkey move (jump x)
            for(int i=0; i<4; ++i){
                int nx = x+inc_x[i], ny = y+inc_y[i];
                if(nx<0 | nx>=h | ny<0 | ny>=w) continue;
                if(nx == (h-1) and ny == (w-1)){
                    cout << move_cnt;
                    return;
                }
                if(board[nx][ny] == 0 and visited[nx][ny] > jump_cnt){
                    visited[nx][ny] = jump_cnt;
                    q.push({jump_cnt, nx, ny});
                }
            }

            // horse move (jump o)
            if(jump_cnt == k) continue;
            for(int i=0; i<8; ++i){
                int nx = x+inc_hx[i], ny = y+inc_hy[i];
                if(nx<0 | nx>=h | ny<0 | ny>=w) continue;
                if(nx == (h-1) and ny == (w-1)){
                    cout << move_cnt;
                    return;
                }
                if(board[nx][ny] == 0 and visited[nx][ny] > (jump_cnt+1)){
                    visited[nx][ny] = jump_cnt+1;
                    q.push({jump_cnt+1, nx, ny});
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