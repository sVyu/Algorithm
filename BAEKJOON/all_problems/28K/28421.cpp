#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, q; cin >> n >> q;
    vector<int> zs(n); for(auto &z:zs) cin >> z;

    int mx = 10000;
    int cnts[mx+1];
    for(int i=0; i<=mx; ++i) cnts[i]=0;
    for(int z:zs) ++cnts[z];

    while(q--){
        int cmd, k; cin >> cmd >> k;

        if(cmd == 1){
            if(k == 0){
                if(cnts[0] >= 1 and n >= 2) cout << "1\n";
                else                        cout << "0\n";
                continue;
            }

            bool pos = false;
            for(int val=1; val<=mx; ++val){
                if(cnts[val] == 0) continue;
                if((k%val) != 0) continue;
                if((k/val) > mx) continue;

                --cnts[val];
                if(cnts[k/val]) pos = true;
                ++cnts[val];
                if(pos) break;
            }
            if(pos) cout << "1\n";
            else    cout << "0\n";
        }else{
            --k;
            --cnts[zs[k]];
            zs[k] = 0;
            ++cnts[0];
            // for(int i=0; i<=10; ++i){
            //     cout << cnts[i] << ' ';
            // }
            // cout << '\n';
        }
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}