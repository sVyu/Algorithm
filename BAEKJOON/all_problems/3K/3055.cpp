#include <bits/stdc++.h>
using namespace std;
// #define pii pair<int,int>

struct dot{
    int x;
    int y;
};


void solve(){
    int h, w; cin >> h >> w;
    string board[h]; for(auto &r:board) cin >> r;

    queue<dot> hq; // hedgehog
    queue<dot> wq; // water
    for(int x=0; x<h; ++x){
        for(int y=0; y<w; ++y){
            if(board[x][y] == 'S') hq.push({x, y});
            if(board[x][y] == '*') wq.push({x, y});
        }
    }

    int px[4] = {0, 1, 0, -1};
    int py[4] = {1, 0, -1, 0};
    int move_cnt = 1;

    // bfs
    while(!hq.empty()){
        // 물의 이동
        int wq_sz = wq.size();
        while(wq_sz--){
            auto [x, y] = wq.front(); wq.pop();
            for(int i=0; i<4; ++i){
                int nx=x+px[i], ny=y+py[i];
                if(nx<0 | nx>=h | ny<0 | ny>=w) continue;
                if(board[nx][ny] == '.'){
                    board[nx][ny] = '*';
                    wq.push({nx, ny});
                }
            }
        }

        // 고슴도치의 이동
        int hq_sz = hq.size();
        while(hq_sz--){
            auto [x, y] = hq.front(); hq.pop();
            for(int i=0; i<4; ++i){
                int nx=x+px[i], ny=y+py[i];
                if(nx<0 | nx>=h | ny<0 | ny>=w) continue;
                if(board[nx][ny] == '.'){
                    board[nx][ny] = 'S';
                    hq.push({nx, ny});
                }
                else if(board[nx][ny] == 'D'){
                    cout << move_cnt; // 탈출 성공
                    return;
                }
            }
        }

        ++move_cnt;
    }

    cout << "KAKTUS" << '\n';
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}