#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, m; cin >> n >> m;
    vector<vector<int>> zs(n, vector<int>(m));
    for(auto &r:zs) for(auto &c:r) cin >> c;

    vector<int> rows(n, 0);
    vector<int> columns(m, 0);
    for(int x=0; x<n; x++){
        for(int y=0; y<m; y++){
            rows[x] += zs[x][y];
            columns[y] += zs[x][y];
        }
    }

    int mx = -int(1e7);
    for(int x1=0; x1<(n-1); x1++){
        for(int x2=(x1+1); x2<n; x2++){
            for(int y1=0; y1<(m-1); y1++){
                for(int y2=(y1+1); y2<m; y2++){
                    int val = rows[x1]+rows[x2]+columns[y1]+columns[y2];
                    val -= (zs[x1][y1]+zs[x1][y2]+zs[x2][y1]+zs[x2][y2]);
                    val += (x2-1-x1)*(y2-1-y1);

                    mx = max(mx, val);
                }
            }
        }
    }

    cout << mx;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}