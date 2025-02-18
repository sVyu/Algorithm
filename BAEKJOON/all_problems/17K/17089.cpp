#include <bits/stdc++.h>
using namespace std;
#define pii pair<int, int>

int main(void){
    int n, m; cin >> n >> m;

    int relations[n+1][n+1];
    fill(&relations[0][0], &relations[0][0]+(n+1)*(n+1), 0);

    queue<pii> q;
    for(int i=0; i<m; ++i){
        int a, b; cin >> a >> b;
        relations[a][b] = 1;
        relations[b][a] = 1;
        q.push({a, b});
    }

    // sums init
    int sums[n+1];
    fill(sums, sums+(n+1), 0);

    for(int i=1; i<=n; ++i){
        int sum = 0;
        for(int j=1; j<=n; ++j) sum += relations[i][j];
        sums[i] = sum;
    }

    // for(int i=1; i<=n; ++i){
    //     cout << sums[i] << '\n';
    // }

    // 2중 for문 로직을 미리 생각해야 됐음
    // next permutation 방법도 한 번 오랜만에 복기하면 좋을 듯
    // 최댓값이 아니라 최솟값이었다니

    int ans = INT_MAX;
    while(!q.empty()){
        auto [a, b] = q.front(); q.pop();
        for(int i=1; i<=n; ++i){
            if(i == a | i == b) continue;
            if(relations[a][i] and relations[b][i]){
                ans = min(ans, sums[a]+sums[b]+sums[i]-6);
            }
        }
    }

    if(ans == INT_MAX) ans = -1;
    cout << ans;
}

