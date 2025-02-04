#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    int mx = 101;
    vector<vector<int>> board(mx, vector<int>(mx));
    vector<vector<int>> cnts(mx, vector<int>(mx, 0));
    vector<vector<int>> sums(mx, vector<int>(mx));

    for(int i=0; i<n; ++i){ // ++n
        int x, y; cin >> x >> y;
        for(int px=0; px<10; ++px){
            ++cnts[x+px][y];
            --cnts[x+px][y+10];
        }
    }

    // for(int x=0; x<30; ++x){
    //     for(int y=0; y<30; ++y){
    //         cout << cnts[x][y] << ' ';
    //     }
    //     cout << '\n';
    // }

    for(int x=0; x<mx; ++x){
        int val = 0;
        for(int y=0; y<mx; ++y){
            val += cnts[x][y];
            board[x][y] = val;
        }
    }

    for(int x=1; x<mx; ++x){
        for(int y=1; y<mx; ++y){
            sums[x][y] = (board[x][y] >= 1) ? 1 : 0;
            sums[x][y] += sums[x-1][y]+sums[x][y-1]-sums[x-1][y-1];
        }
    }

    int ans = 0;
    // bx, by : base_dot
    for(int bx=1; bx<mx; ++bx){
        for(int by=1; by<mx; ++by){

            // px, py : plux_x, plus_y
            int kx = mx-bx, ky = mx-by;
            for(int px=0; px<kx; ++px){
                for(int py=0; py<ky; ++py){

                    // 두 점을 기준으로 사각형을 그렸을 때 내부가 다 채워져 있는 경우 ans 갱신
                    // 두 점 기준 : bruteforce
                    int nx = bx+px, ny = by+py;
                    int area = (nx-bx+1)*(ny-by+1);
                    if(sums[nx][ny]-sums[nx][by-1]-sums[bx-1][ny]+sums[bx-1][by-1] == area){
                        ans = max(ans, area);
                    }
                }
            }
        }
    }

    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}