#include <bits/stdc++.h>
using namespace std;

struct dot{
    int x;
    int y;
    int area_cnt;
};

int fp(vector<int> &parent, int x){
    if(parent[x] == x) return x;
    return parent[x] = fp(parent, parent[x]);
}

void up(vector<int> &parent, int a, int b){
    int pa = fp(parent, a);
    int pb = fp(parent, b);

    if(pa > pb) parent[pa] = pb;
    else        parent[pb] = pa;
}

void solve(){
    int h, w; cin >> h >> w;
    vector<vector<char>> board(h, vector<char>(w));
    for(auto &row:board) for(auto &el:row) cin >> el;

    // for(auto r:board){
    //     for(auto el:r) cout << el;
    //     cout << '\n';
    // }

    vector<vector<bool>> visited(h, vector<bool>(w, false));
    vector<vector<int>> area_nums(h, vector<int>(w, 0));
    vector<int> parent({0});

    int px[4] = {0, 1, 0, -1};
    int py[4] = {1, 0, -1, 0};

    int area_cnt = 0;
    queue<dot> q, tmp_q;
    for(int x=0; x<h; ++x){
        for(int y=0; y<w; ++y){
            if(!visited[x][y] and (board[x][y] == '.' || board[x][y] == 'L')){
                visited[x][y] = true;
                area_nums[x][y] = ++area_cnt;
                parent.push_back(area_cnt);
                q.push({x, y, area_cnt});

                while(!q.empty()){
                    auto [bx, by, tmp] = q.front(); q.pop();
                    area_nums[bx][by] = area_cnt;

                    for(int i=0; i<4; ++i){
                        int nx=bx+px[i], ny=by+py[i];
                        if((nx<0)|(nx>=h)|(ny<0)|(ny>=w)) continue;
                        if(parent[area_nums[nx][ny]] != 0) up(parent, area_nums[nx][ny], area_cnt);
                        if(visited[nx][ny]) continue;

                        if(board[nx][ny] == '.' || board[nx][ny] == 'L'){
                            visited[nx][ny] = true;
                            q.push({nx, ny, area_cnt});
                        }
                        else if(board[nx][ny] == 'X'){
                            visited[nx][ny] = true;
                            tmp_q.push({nx, ny, area_cnt});
                        }
                    }
                }
            }
        }
    }

    // for(auto r:area_nums){
    //     for(auto el:r) cout << el;
    //     cout << '\n';
    // }
    // cout << '\n';

    vector<dot> lxys;
    for(int x=0; x<h; ++x){
        for(int y=0; y<w; ++y){
            if(board[x][y] == 'L') lxys.push_back({x, y});
        }
    }

    q = tmp_q; // deep_copy
    int parent_sz = parent.size();
    int day = 0;

    while(!q.empty()){
        for(int i=1; i<parent_sz; ++i) fp(parent, i); // required
        // for(auto p:parent) cout << p << ' '; cout << '\n';
        auto [lx1, ly1, tmp1] = lxys[0];
        auto [lx2, ly2, tmp2] = lxys[1];
        if(parent[area_nums[lx1][ly1]] == parent[area_nums[lx2][ly2]]) break;

        int q_sz = q.size();
        while(q_sz--){
            auto [x, y, area_cnt] = q.front(); q.pop();
            area_nums[x][y] = area_cnt;
            for(int i=0; i<4; ++i){
                int nx = x+px[i], ny = y+py[i];
                if((nx<0)|(nx>=h)|(ny<0)|(ny>=w)) continue;
                if(parent[area_nums[nx][ny]] != 0 and parent[area_nums[nx][ny]] != area_cnt){
                    up(parent, area_nums[nx][ny], area_cnt);
                }
                if(visited[nx][ny]) continue;

                if(board[nx][ny] == 'X'){
                    visited[nx][ny] = true;
                    q.push({nx, ny, area_cnt});
                }
            }
        }
        ++day;
    }

    // for(int i=1; i<parent_sz; ++i) fp(parent, i); // required
    // for(auto p:parent) cout << p << ' '; cout << '\n';

    cout << day;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}