#include <bits/stdc++.h>
using namespace std;

int px[4] = {0, 1, 0, -1};
int py[4] = {1, 0, -1, 0};

struct dot{
    int x;
    int y;
};

void solve(){
    int n; cin >> n;
    vector<string> board(n); for(auto &r:board) cin >> r;

    bool visited[n][n];
    for(int x=0; x<n; ++x) for(int y=0; y<n; ++y) visited[x][y] = false;

    int largest_area = -1;
    int smallest_perimeter = INT_MAX;

    for(int x=0; x<n; ++x){
        for(int y=0; y<n; ++y){
            if(!visited[x][y] and board[x][y] == '#'){
                visited[x][y] = true;
                int ta = 0, tp = 0;
                queue<dot> q({{x, y}});

                while(!q.empty()){
                    auto [tx, ty] = q.front(); q.pop();
                    ta++;
                    for(int i=0; i<4; ++i){
                        int nx = tx+px[i], ny = ty+py[i];
                        if(nx < 0 | nx >= n | ny < 0 | ny >= n){
                            tp++;
                            continue;
                        }

                        if(board[nx][ny] == '.'){
                            tp++;
                        }
                        else if(board[nx][ny] == '#' and !visited[nx][ny]){  
                            // ta++;
                            visited[nx][ny] = true;
                            q.push({nx, ny});
                        }
                    }
                }

                if(largest_area < ta){
                    largest_area = ta;
                    smallest_perimeter = tp;
                }else if(largest_area == ta){
                    smallest_perimeter = tp;
                }
            }
        }
    }
    
    cout << largest_area << ' ' << smallest_perimeter;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}