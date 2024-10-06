#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, k; cin >> n >> k;
    vector<vector<int>> dists(n, vector<int>(n));
    for(auto &ds:dists) for(auto &d:ds) cin >> d;

    // floyd-warshall
    for(int i=0; i<n; i++){
        for(int a=0; a<n; a++){
            for(int b=0; b<n; b++){
                dists[a][b] = min(dists[a][b], dists[a][i]+dists[i][b]);
            }
        }
    }

    // all_permutation
    int ans = 1e4;
    vector<int> orders;
    for(int i=0; i<n; i++) if(i != k) orders.push_back(i);

    do{
        int s = -1, e = k, sum_dists = 0;
        for(auto o:orders){
            s = e; e = o;
            sum_dists += dists[s][e];
        }
        ans = min(ans, sum_dists);
    }while(next_permutation(orders.begin(), orders.end()));

    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}