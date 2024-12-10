#include <bits/stdc++.h>
using namespace std;

void solve(){
    int m, n; cin >> m >> n;
    int k; cin >> k;
    vector<string> board(m); for(auto &r:board) cin >> r;
    int cnts[m+1][n+1][3];
    fill(&cnts[0][0][0], &cnts[0][0][0]+(m+1)*(n+1)*3, 0);

    for(int x=1; x<=m; ++x){
        for(int y=1; y<=n; ++y){
            for(int i=0; i<3; ++i){
                cnts[x][y][i] = cnts[x-1][y][i]+cnts[x][y-1][i]-cnts[x-1][y-1][i];
            }
            if(board[x-1][y-1] == 'J')      ++cnts[x][y][0];
            else if(board[x-1][y-1] == 'O') ++cnts[x][y][1];
            else                            ++cnts[x][y][2];
        }
    }

    while(k--){
        int a, b, c, d; cin >> a >> b >> c >> d;
        for(int i=0; i<3; ++i){
            cout << cnts[c][d][i]-cnts[a-1][d][i]-cnts[c][b-1][i]+cnts[a-1][b-1][i] << ' ';
        }
        cout << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}