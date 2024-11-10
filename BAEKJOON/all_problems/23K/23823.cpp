#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, q; cin >> n >> q;
    vector<int> rows(n+1, 0), cols(n+1, 0);
    int max_row_val = 0, max_row_cnt = n;
    int max_col_val = 0, max_col_cnt = n;

    while(q--){
        int t, a; cin >> t >> a;
        if(t == 1){
            rows[a]++;
            if(max_row_val == rows[a]){
                max_row_cnt++;
            }
            else if (max_row_val < rows[a]){
                max_row_val = rows[a];
                max_row_cnt = 1;
            }
        }else{
            cols[a]++;
            if(max_col_val == cols[a]){
                max_col_cnt++;
            }
            else if (max_col_val < cols[a]){
                max_col_val = cols[a];
                max_col_cnt = 1;
            }
        }

        cout << max_row_cnt*max_col_cnt << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}