#include <bits/stdc++.h>
using namespace std;

int solve(){
    int n, m, l, k;
    cin >> n >> m >> l >> k;

    int dots[k][2];
    for(int i=0; i<k; i++) for(int j=0; j<2; j++) cin >> dots[i][j];
    int dx[4] = {0, 0, 1, 1};
    int dy[4] = {0, 1, 0, 1};

    // reflextion
    int max_refl = 0;
    for(int i=0; i<k; i++){
        for(int j=0; j<k; j++){
            int x = dots[i][0], y = dots[j][1];
            for(int d=0; d<4; d++){
                int bx = x+dx[d], by = y+dy[d];

                int tmp_refl = 0;
                for(int a=0; a<k; a++){
                    if((bx-1) <= dots[a][0] and dots[a][0] <= (bx+l) and
                        (by-1) <= dots[a][1] and dots[a][1] <= (by+l))
                        tmp_refl++;
                max_refl = max(max_refl, tmp_refl);
                }
            }
        }
    }

    cout << k-max_refl;
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}