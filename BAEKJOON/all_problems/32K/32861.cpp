#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    int board[n][n];

    for(int i=0; i<n; ++i){
        for(int j=0; j<n; ++j){
            int k; cin >> k;
            board[i][j] = k;
        }
    }

    bool visited[n+1];
    fill(visited, visited+n+1, false);
    int ans[n]={0,};

    for(int x=0; x<n; ++x){
        int one_cnt=0;
        for(int y=0; y<n; ++y){
            // cout << x << ' ' << y << '\n';
            if(x==y and board[x][y] != 0){
                cout << -1;
                return;
            }
            if(x!=y and ((board[x][y] == 0) || (board[x][y]==board[y][x]))){
                cout << -1;
                return;
            }
            if(board[x][y] == 1) ++one_cnt;
        }

        int val = n-one_cnt;
        if(val <= 0 || val > n){
            cout << -1;
            return;
        }
        if(visited[val]){
            cout << -1;
            return;
        }
        visited[val] = true;
        ans[x] = val;
    }
    for(int i=0; i<n; ++i) cout << ans[i] << ' ';
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}