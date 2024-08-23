#include <bits/stdc++.h>
using namespace std;

int solve(){
    int n; cin >> n;
    int ns[n][5];
    for(int i=0; i<n; i++) for(int j=0; j<5; j++) cin >> ns[i][j];

    bool check[n][n];
    fill(&check[0][0], &check[0][0]+n*n, 0);

    for(int i=0; i<n-1; i++){
        for(int j=i+1; j<n; j++){
            for(int k=0; k<5; k++){
                if(ns[i][k] == ns[j][k]){
                    check[i][j] = true;
                    check[j][i] = true;
                    break;
                }
            }
        }
    }

    int ans_idx = -1, ans_cnt = -1;
    for(int i=0; i<n; i++){
        int sum_cnt = 0;
        for(int j=0; j<n; j++) if(check[i][j]) sum_cnt++;

        if(ans_cnt < sum_cnt){
            ans_idx = i;
            ans_cnt = sum_cnt;
        }
    }

    cout << ans_idx+1 << '\n';
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}