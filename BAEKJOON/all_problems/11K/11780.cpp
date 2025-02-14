#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, m; cin >> n >> m;

    int board[n][n];
    int mx = int(1e8);
    fill(&board[0][0], &board[0][0]+(n*n), mx);
    vector<int> routes[n][n];
    for(int i=0; i<n; ++i) board[i][i] = 0;

    while(m--){
        int a, b, c; cin >> a >> b >> c;
        --a; --b;
        if(board[a][b] > c){
            board[a][b] = c;
            routes[a][b] = {a, b};
        }
    }

    // for(int i=0; i<n; ++i){
    //     for(int j=0; j<n; ++j){
    //         cout << board[i][j] << ' ';
    //     }
    //     cout << '\n';
    // }

    for(int k=0; k<n; ++k){
        for(int a=0; a<n; ++a){
            for(int b=0; b<n; ++b){
                if(a==b) continue;
                int new_val = board[a][k]+board[k][b];
                if(board[a][b] > new_val){
                    board[a][b] = new_val;
                    routes[a][b] = routes[a][k];
                    routes[a][b].pop_back();
                    for(int el:routes[k][b]) routes[a][b].push_back(el);
                }
            }
        }
    }

    for(int i=0; i<n; ++i){
        for(int j=0; j<n; ++j){
            int val = (board[i][j] != mx) ? board[i][j] : 0; // 
            cout << val << ' ';
        }
        cout << '\n';
    }

    for(int i=0; i<n; ++i){
        for(int j=0; j<n; ++j){
            int sz = routes[i][j].size();
            cout << sz << ' ';
            if(sz != 0) for(auto el:routes[i][j]) cout << el+1 << ' ';
            cout << '\n';
        }
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}