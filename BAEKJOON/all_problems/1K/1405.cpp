#include <bits/stdc++.h>
using namespace std;

int px[4] = {0, 0, 1, -1};
int py[4] = {1, -1, 0, 0};

void btr(int n, int move_cnt, int x, int y, bool board[][50], double& ans, vector<double>& prcts, double val){
    board[x][y] = true;
    if(n == move_cnt){
        ans += val;
        board[x][y] = false;
        return;
    }

    for(int p=0; p<4; ++p){
        int nx = x+px[p], ny = y+py[p];
        if(board[nx][ny]) continue;
        if(prcts[p] == 0) continue;
        btr(n, move_cnt+1, nx, ny, board, ans, prcts, val*(prcts[p]/100));
    }
    board[x][y] = false;
}

int main(void){
    int n; cin >> n;
    vector<double> prcts(4); for(auto &prct:prcts) cin >> prct;

    double ans = 0.0;
    bool board[50][50];
    fill(&board[0][0], &board[0][0]+50*50, false);

    board[25][25] = true;
    btr(n, 0, 25, 25, board, ans, prcts, 1);

    cout << fixed;
    cout.precision(10);
    cout << ans;
}