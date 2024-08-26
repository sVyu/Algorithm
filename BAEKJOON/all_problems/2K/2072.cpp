#include <bits/stdc++.h>
using namespace std;

const int sz = 21;
int board[sz][sz];
int dx[4] = {-1, -1, 0, 1};
int dy[4] = {0, 1, 1, 1};

bool win_check(int x, int y, int c){
    for(int d=0; d<4; d++){
        int cnt = -1;

        int tx = x, ty = y;
        while(board[tx][ty] == c){
            tx -= dx[d];
            ty -= dy[d];
            cnt++;
        }
        tx = x; ty = y;
        while(board[tx][ty] == c){
            tx += dx[d];
            ty += dy[d];
            cnt++;
        }

        if(cnt == 5) return true;
    }
    return false;
}

int solve(){
    int n; cin >> n;
    int c = 0; // color;

    for(int t=1; t<=n; t++){
        int x, y;
        cin >> x >> y;

        board[x][y] = c;
        if(win_check(x, y, c)){
            cout << t;
            return 0;
        }
        c = (c+1)%2;
    }

    cout << -1;
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    fill(&board[0][0], &board[0][0]+sz*sz, -1);
    solve();
    return 0;
}

