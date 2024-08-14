#include <iostream>
#include <vector>
using namespace std;

int btr(vector<vector<int>> times, vector<bool> visited, int N, int v, int cnt, int tot_time, int* ans){
    if(cnt == N and times[v][0] != -1){
        *ans = max(*ans, tot_time+times[v][0]);
        // cout << "haha" << tot_time+times[v][0] << '\n';
        // cout << *ans << '\n';
        return 0;
    }

    for(int next=1; next<=N; next++){
        if(next==v) continue;
        if(!visited[next] and times[v][next] != -1){
            visited[next] = true;
            btr(times, visited, N, next, cnt+1, tot_time+times[v][next], ans);
            visited[next] = false;
        }
    }
    return 0;
}

void solve(){
    int N; cin >> N;
    int M; cin >> M;

    vector<vector<int>> times(N+1, vector<int>(N+1, -1));
    while(M--){
        int u, v, d;
        cin >> u >> v >> d;
        times[u][v] = max(times[u][v], d);
    }

    // for(int x=0; x<=N; x++){
    //     for(int y=0; y<=N; y++){
    //         cout << times[x][y] << ' ';
    //     }
    //     cout << '\n';
    // }

    vector<bool> visited(N+1, false);
    // for(int x=0; x<=N; x++) cout << visited[x] << ' ';

    int ans = -1;
    btr(times, visited, N, 0, 0, 0, &ans);
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();
    return 0;
}