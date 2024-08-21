#include <bits/stdc++.h>
using namespace std;
// typedef long long ll;

int solve(){
    int N; cin >> N;
    vector<vector<int>> vvts(N);
    for(int i=0; i<N; i++){
        int k; cin >> k;
        while(k--){
            int t; cin >> t;
            vvts[i].push_back(t);
        }
    }

    int M; cin >> M;
    while(M--){
        int p; cin >> p;
        bool empty[51]={0};
        while(p--){
            int q; cin >> q;
            empty[q] = true;
        }

        int cnt = 0;
        for(int i=0; i<N; i++){
            bool pos = true;
            for(auto t:vvts[i]){
                if(!empty[t]){      //
                    pos=false;
                    break;
                }
            }

            if(pos) cnt++;
        }
        cout << cnt << '\n';
    }
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}