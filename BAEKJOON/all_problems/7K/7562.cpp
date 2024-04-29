#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    while(n--){
        int l;
        cin >> l;

        int x, y;
        cin >> x >> y;
        int tx, ty; // target
        cin >> tx >> ty;

        if(x==tx and y==ty){
            cout << 0 << '\n';
            continue;
        }

        vector<vector<int>> board(l, vector<int>(l, 0));
        vector<vector<bool>> visited(l, vector<bool>(l, false));
        vector<int> inc_xy[8];
        inc_xy[0] = {2, 1};
        inc_xy[1] = {1, 2};
        inc_xy[2] = {-1, 2};
        inc_xy[3] = {-2, 1};
        inc_xy[4] = {-2, -1};
        inc_xy[5] = {-1, -2};
        inc_xy[6] = {1, -2};
        inc_xy[7] = {2, -1};

        int ans = 0;
        queue<vector<int>> q;
        q.push({x, y});

        visited[x][y] = true;
        bool found = false;
        while(!q.empty()){
            ans += 1;
            int q_size = q.size();
            for(int i=0; i<q_size; i++){
                vector<int> xy = q.front();
                q.pop();

                int nx, ny;
                for(auto pxy:inc_xy){
                    nx = xy[0]+pxy[0];
                    ny = xy[1]+pxy[1];
                    if(0<=nx && nx<l && 0<=ny && ny<l && !visited[nx][ny]){
                        if(nx==tx && ny==ty){
                            found = true;
                            break;
                        }
                        q.push({nx, ny});
                        visited[nx][ny] = true;
                    }
                }
                if(found) break;
            }
            if(found) break;
        }
        cout << ans << '\n';
    }
}