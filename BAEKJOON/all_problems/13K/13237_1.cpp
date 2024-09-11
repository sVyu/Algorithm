#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    vector<int> ps(n, 0);
    for(auto &p:ps){
        int k; cin >> k;
        p = k-1;
    }

    int cnt=1;
    int now_lv=0;
    int lvs[n]{};

    vector<int> vs;
    for(int i=0; i<n; i++) if(ps[i]==-2) vs.push_back(i);

    while(cnt<n){
        vector<int> new_vs;
        for(int i=0; i<n; i++){
            if(lvs[i]) continue;
            for(auto v:vs){
                if(ps[i] == v){
                    new_vs.push_back(i);
                    lvs[i]=now_lv+1;
                    cnt++;
                    break;
                }
            }
        }

        vs=new_vs;
        now_lv++;
    }

    for(auto lv:lvs) cout << lv << '\n';
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}