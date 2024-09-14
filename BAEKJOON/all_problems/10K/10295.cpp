#include <bits/stdc++.h>
using namespace std;

struct pt{
    int x;
    int y;
    int c;  // cost
};

const int mx = 1e7;
int dx[8]={0, 1, 1, 1, 0, -1, -1, -1};
int dy[8]={1, 1, 0, -1, -1, -1, 0, 1};

void solve(){
    int t; cin >> t;
    while(t--){
        int h, w; cin >> h >> w;
        vector<string> board(h);
        for(auto &r:board) cin >> r;

        int x, y; cin >> x >> y;
        queue<pt> q({{x, y, 0}});

        vector<vector<int>> costs(h, vector<int>(w, mx));
        costs[x][y]=0;
        while(!q.empty()){
            auto [x, y, c] = q.front(); q.pop();
            for(int d=0; d<8; d++){
                int nx=x+dx[d];
                int ny=y+dy[d];
                if(nx < 0 | nx >= h | ny < 0 | ny >= w) continue;
                if(board[nx][ny] == '#') continue;

                int nc = c+pow(abs(board[x][y]-board[nx][ny])+1, 2);
                if(costs[nx][ny] > nc){
                    costs[nx][ny] = nc;
                    q.push({nx, ny, nc});
                }
            }
        }

        pt highest={-1, -1, -1};
        for(int x=0; x<h; x++){
            for(int y=0; y<w; y++){
                char c = board[x][y];
                if(c=='#') continue;
                if(highest.c < (c-'0')) highest = {x, y, c-'0'};
            }
        }

        if(costs[highest.x][highest.y] == mx){
            cout << "NO" << '\n';
            continue;
        }
        cout << costs[highest.x][highest.y] << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    solve();
    return 0;
}

/*

2
3 3
1##
##2
##3
0 0
5 5
11111
1###1
12341
12221
12221
0 0
*/