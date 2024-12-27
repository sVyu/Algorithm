#include <bits/stdc++.h>
using namespace std;

bool check_bingo(vector<vector<bool>> &visited){
    int cnt=0;
    for(int i=0; i<5; ++i){ // คั
        bool pos = true;
        for(int j=0; j<5; ++j) if(!visited[i][j]) pos = false;
        if(pos) ++cnt;
    }
    for(int j=0; j<5; ++j){ // |
        bool pos = true;
        for(int i=0; i<5; ++i) if(!visited[i][j]) pos = false;
        if(pos) ++cnt;
    }

    bool pos = true;
    for(int i=0; i<5; ++i){ // "\"
        if(!visited[i][i]) pos = false;
    }
    if(pos) ++cnt;

    pos = true;
    for(int i=0; i<5; ++i){ // "/"
        if(!visited[i][4-i]) pos = false;
    }
    if(pos) ++cnt;

    if(cnt >= 3) return true;
    return false;
}

void solve(){
    vector<vector<int>> board(5, vector<int>(5));
    for(auto &r:board) for(auto &el:r) cin >> el;
    vector<vector<bool>> visited(5, vector<bool>(5, false));

    for(int cnt=1; cnt<=25; ++cnt){
        int n; cin >> n;
        for(int i=0; i<5; ++i){
            for(int j=0; j<5; ++j){
                if(board[i][j] == n){
                    visited[i][j] = true;
                    if(check_bingo(visited)){
                        cout << cnt;
                        return;
                    }
                }
            }
        }
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}