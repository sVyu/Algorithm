#include <bits/stdc++.h>
using namespace std;

int space_cnt = 0;
int max_area = 0;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;
    vector<vector<int>> board(n, vector<int>(m,0));
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    vector<vector<int>> inc_xy(4, vector<int>(2, 0));

    // init board
    for(int x=0; x<n; x++){
        for(int y=0; y<m; y++){
            cin >> board[x][y];
        }
    }
    // init inc_xy
    inc_xy[0] = {0, 1};
    inc_xy[1] = {1, 0};
    inc_xy[2] = {0, -1};
    inc_xy[3] = {-1, 0};

    queue<vector<int>> q;
    for(int x=0; x<n; x++){
        for(int y=0; y<m; y++){
            if(board[x][y] == 1 and !visited[x][y]){
                q.push({x,y});
                visited[x][y] = true;
                space_cnt += 1;
                // cout << "here" << x << ' ' << y << '\n';

                int area = 1;
                while(!q.empty()){
                    vector<int> xy = q.front();
                    q.pop();
                    // cout << "xy" << ' ' << x << ' ' << y << '\n';
                    for(auto v:inc_xy){
                        int nx, ny;
                        nx = xy[0]+v[0];
                        ny = xy[1]+v[1];

                        if(0<=nx and nx<n and 0<=ny and ny<m and board[nx][ny] == 1 and !visited[nx][ny]){
                            // cout << "nx, ny" << nx << ny << '\n';
                            q.push({nx,ny});
                            visited[nx][ny] = true;
                            area += 1;
                        }
                    }
                }
                max_area = max(max_area, area);
            }
        }
    }
    cout << space_cnt << '\n';
    cout << max_area << '\n';
}