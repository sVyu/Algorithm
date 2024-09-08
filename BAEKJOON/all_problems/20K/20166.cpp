#include <bits/stdc++.h>
using namespace std;

int n, m, k;
int dx[8]={0, 1, 1, 1, 0, -1,-1, -1};
int dy[8]={1, 1, 0, -1, -1, -1, 0, 1};

void dfs(vector<string> board, int x, int y, int &cnt, int len_now, string target, int len_target){
    if(len_now == len_target) cnt++;

    for(int d=0; d<8; d++){
        int nx=(n+x+dx[d])%n, ny=(m+y+dy[d])%m;
        if(board[nx][ny] != target[len_now]) continue;
        dfs(board, nx, ny, cnt, len_now+1, target, len_target);
    }
}

void solve(){
    cin >> n >> m >> k;
    vector<string> board(n);
    for(auto &r:board) cin >> r;

    map<string, int> smap;
    while(k--){
        string target; cin >> target;
        if(!smap.count(target)){
            int cnt=0;
            for(int x=0; x<n; x++){
                for(int y=0; y<m; y++){
                    if(board[x][y] != target[0]) continue;
                    dfs(board, x, y, cnt, 1, target, target.length());
                }
            }
            smap[target]=cnt;
        }
        cout << smap[target] << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}