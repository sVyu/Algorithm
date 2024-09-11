#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, e, t, m;
    cin >> n >> e >> t >> m;

    // int mx = INT_MAX;
    int mx = 1e6;
    int sz=n+1;
    int dists[sz][sz];
    fill(&dists[0][0], &dists[0][0]+sz*sz, mx);

    for(int i=0; i<m; i++){
        int a, b, val;
        cin >> a >> b >> val;
        dists[a][b] = min(dists[a][b], val);
    }

    // floyd_warshall
    for(int k=0; k<sz; k++){
        for(int i=0; i<sz; i++){
            for(int j=0; j<sz; j++){
                dists[i][j] = min(dists[i][j], dists[i][k]+dists[k][j]);
            }
        }
    }

    int ans=1;
    for(int i=1; i<sz; i++){
        if(i==e) continue;
        if(dists[i][e] <= t) ans++;
    }
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}