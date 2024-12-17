#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, m; cin >> n >> m;
    vector<int> xs(n, 1);
    vector<int> ys(m, 1);

    for(int x=0; x<n; ++x){
        for(int y=0; y<m; ++y){
            char c; cin >> c;
            if(c=='X'){
                xs[x]=0;
                ys[y]=0;
            }
        }
    }

    cout << max(accumulate(xs.begin(),xs.end(),0), accumulate(ys.begin(),ys.end(),0));
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}