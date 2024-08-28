#include <bits/stdc++.h>
using namespace std;

void solve(){
    int w, h; cin >> w >> h;
    while(w and h){
        vector<vector<int>> ver(h, vector<int>(w-1, 0));
        vector<vector<int>> hor(h-1, vector<int>(w, 0));

        bool vt = true;         // ver_turn
        int i=0;
        int input_times = 2*h-1;

        while(input_times--){   //
            if(vt){
                for(int j=0; j<w-1; j++) cin >> ver[i][j];
            }else{
                for(int j=0; j<w; j++) cin >> hor[i][j];
                i++;
            }
            vt = !vt;           //
        }

        queue<pair<int, int>> q({{0, 0}});
        vector<vector<bool>> visited(h, vector<bool>(w, false));
        visited[0][0] = true;

        int step = 0;
        bool find = false;
        while(!q.empty()){
            ++step;
            int q_size = q.size();
            while(q_size--){
                auto [x, y] = q.front(); q.pop();
                if(x == h-1 and y == w-1){
                    cout << step << '\n';
                    find = true;
                    break;
                }

                if(y < (w-1) and !visited[x][y+1] and ver[x][y] == 0){
                    q.push({x, y+1});
                    visited[x][y+1] = true;
                }
                if(x < (h-1) and !visited[x+1][y] and hor[x][y] == 0){
                    q.push({x+1, y});
                    visited[x+1][y] = true;
                }
                if(y > 0 and !visited[x][y-1] and ver[x][y-1] == 0){
                    q.push({x, y-1});
                    visited[x][y-1] = true;
                }
                if(x > 0 and !visited[x-1][y] and hor[x-1][y] == 0){
                    q.push({x-1, y});
                    visited[x-1][y] = true;
                }
            }
            if(find) break;
        }
        if(!find) cout << 0 << '\n';
        cin >> w >> h;
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}