#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    vector<vector<char>> board(n, vector<char>(n));
    for(auto &r:board) for(auto &el:r) cin >> el;

    // for(auto r:board){
    //     for(auto el:r) cout << el;
    //     cout << '\n';
    // }

    int cnt = 0;
    for(int i=n-1; i>=0; --i){
        for(int j=n-1; j>=0; --j){
            if(board[i][j] == '1'){
                ++cnt;
                for(int a=i; a>=0; --a){
                    for(int b=j; b>=0; --b){
                        if(board[a][b] == '1')  board[a][b] = '0';
                        else                    board[a][b] = '1';
                    }
                }
            }
        }
    }
    cout << cnt;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}