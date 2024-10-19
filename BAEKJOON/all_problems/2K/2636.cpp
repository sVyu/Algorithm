#include <bits/stdc++.h>
using namespace std;

struct dot{
    int x;
    int y;
};

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

void solve(){
    int h, w; cin >> h >> w;
    vector<vector<int>> board(h, vector<int>(w));
    for(auto &r:board) for(auto &el:r) cin >> el;

    queue<dot> q({{0,0}});
    vector<vector<bool>> visited(h, vector<bool>(w, false));
    visited[0][0] = true;
    int turn = 0, cnt = 0;

    while(!q.empty()){
        queue<dot> nq;
        int tmp_cnt = 0;

        while(!q.empty()){
            auto [x, y] = q.front(); q.pop();

            for(int d=0; d<4; d++){
                int nx = x+dx[d], ny = y+dy[d];
                if(nx < 0 | nx >= h | ny < 0 | ny >= w) continue; //
                if(visited[nx][ny]) continue;
                visited[nx][ny] = true;

                if(board[nx][ny] == 0){
                    q.push({nx, ny});
                }
                else{ // board[nx][ny] == 1
                    board[nx][ny] = 0;
                    nq.push({nx, ny});
                    tmp_cnt++;
                }
            }
        }

        if(nq.empty()){
            cout << turn << '\n' << cnt;
            return;
        }

        q = nq;
        turn++;
        cnt = tmp_cnt;
    }

    return;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}