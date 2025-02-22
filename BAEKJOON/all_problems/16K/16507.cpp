#include <bits/stdc++.h>
using namespace std;

int main(void){
    int r, c, q; cin >> r >> c >> q;
    int board[r+1][c+1];
    int sums[r+1][c+1];
    fill(&board[0][0], &board[0][0]+(r+1)*(c+1), 0);
    fill(&sums[0][0], &sums[0][0]+(r+1)*(c+1), 0);

    for(int x=1; x<=r; ++x){
        for(int y=1; y<=c; ++y){
            int k; cin >> k;
            board[x][y] = k;
        }
    }

    for(int x=1; x<=r; ++x){
        for(int y=1; y<=c; ++y){
            sums[x][y] = board[x][y]+sums[x-1][y]+sums[x][y-1]-sums[x-1][y-1];
        }
    }

    while(q--){
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        int sum_val = sums[x2][y2]-sums[x1-1][y2]-sums[x2][y1-1]+sums[x1-1][y1-1];
        int sum_area = (x2-x1+1)*(y2-y1+1);
        cout << sum_val/sum_area << '\n';
    }
}