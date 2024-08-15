#include <iostream>
#include <vector>
#include <queue>
// #include <algorithm>
using namespace std;

bool same_board_check(vector<vector<int>> board1, vector<vector<int>> board2, int N, int M){
    for(int x=0; x<N; x++){
        for(int y=0; y<M; y++){
            if(board1[x][y] != board2[x][y]) return false;
        }
    }
    return true;
}

int solve(){
    int N, M;
    cin >> N >> M;

    vector<vector<int>> board1(N, vector<int>(M,0));
    for(int x=0; x<N; x++) for(int y=0; y<M; y++) cin >> board1[x][y];

    vector<vector<int>> board2(N, vector<int>(M,0));
    for(int x=0; x<N; x++) for(int y=0; y<M; y++) cin >> board2[x][y];

    queue<vector<int>> q;
    int inc_x[] = {0, 1, 0, -1};
    int inc_y[] = {1, 0, -1, 0};
    bool visited[N][M] = {0};
    fill(&visited[0][0], &visited[0][0]+N*M, false);

    for(int x=0; x<N; x++){
        for(int y=0; y<M; y++){
            if(board1[x][y] != board2[x][y]){
                q.push({x, y});
                visited[x][y] = true;
                int origin_color = board1[x][y];
                board1[x][y] = board2[x][y];

                while(!q.empty()){
                    vector<int> xy = q.front(); q.pop();
                    int kx=xy[0], ky=xy[1];

                    for(int i=0; i<4; i++){
                        int nx = kx+inc_x[i], ny = ky+inc_y[i];
                        if(0 <= nx and nx < N and 0 <= ny and ny < M){
                            if((board1[nx][ny] == origin_color) and !visited[nx][ny]){
                                board1[nx][ny] = board2[x][y];
                                visited[nx][ny] = true;
                                q.push({nx, ny});
                            }
                        }
                    }
                }

                if(same_board_check(board1, board2, N, M))
                    cout << "YES";
                else cout << "NO";
                return 0;
            }
        }
    }

    cout << "YES";
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}