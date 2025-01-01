#include <bits/stdc++.h>
using namespace std;

struct dot{
    int x;
    int y;
};

void solve(){
    int n, k; cin >> n >> k;
    vector<vector<int>> board(2, vector<int>(n, 0));
    for(int x=0; x<2; ++x){
        string s; cin >> s;
        for(int y=0; y<n; ++y){
            board[x][y] = s[y]-'0';
        }
    }

    vector<vector<bool>> visited(2, vector<bool>(n, false));
    visited[0][0] = true;
    queue<dot> q({{0, 0}});

    for(int i=0; i<n; ++i){ // ++n...
        board[0][i]=0;
        board[1][i]=0;

        int sz = q.size();
        while(sz--){
            auto [x, y] = q.front(); q.pop();
            if((y+k) >= n){ // includes x+k
                cout << 1;
                return;
            }

            if(board[x][y+1] == 1 and !visited[x][y+1]){
                visited[x][y+1] = true;
                q.push({x, y+1});
            }
            if(y>=1 and board[x][y-1] == 1 and !visited[x][y-1]){ //
                visited[x][y-1] = true;
                q.push({x, y-1});
            }
            if(board[(x+1)%2][y+k] == 1 and !visited[(x+1)%2][y+k]){
                visited[(x+1)%2][y+k] = true;
                q.push({(x+1)%2, y+k});
            }
        }
    }
    cout << 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}