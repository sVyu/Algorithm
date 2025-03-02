#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int n, m; cin >> n >> m;
    int k; cin >> k;

    int check[n+1][m+1][2];
    ll cnts[n+1][m+1];
    for(int x=0; x<=n; ++x){
        for(int y=0; y<=m; ++y){
            for(int z=0; z<2; ++z)
                check[x][y][z]=0;
            cnts[x][y] = 0;
        }
    }
    cnts[0][0] = 1;

    while(k--){
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        if(x1 > x2) swap(x1, x2);
        if(y1 > y2) swap(y1, y2);

        if((x1-x2) < 0) check[x1][y1][0] = 1;
        else            check[x1][y1][1] = 1;
    }

    for(int x=0; x<=n; ++x){
        for(int y=0; y<=m; ++y){
            if(x>0 and (check[x-1][y][0]==0)){
                cnts[x][y] += cnts[x-1][y];
            }
            if(y>0 and (check[x][y-1][1]==0)){
                cnts[x][y] += cnts[x][y-1];
            }
        }
    }

    cout << cnts[n][m];
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}