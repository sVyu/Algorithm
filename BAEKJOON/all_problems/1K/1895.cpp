#include <bits/stdc++.h>
using namespace std;

int main(void){
    int r, c; cin >> r >> c;
    vector<vector<int>> board(r, vector<int>(c, 0));
    for(auto &row:board) for(auto &el:row) cin >> el;

    int t; cin >> t;
    int ans = 0;
    for(int i=0; i<(r-2); i++){
        for(int j=0; j<(c-2); j++){
            vector<int> zs;
            for(int a=0; a<3; a++){
                for(int b=0; b<3; b++){
                    zs.push_back(board[i+a][j+b]);
                }
            }

            sort(zs.begin(), zs.end());
            if(zs[4]>=t) ++ans;
        }
    }

    cout << ans;
}