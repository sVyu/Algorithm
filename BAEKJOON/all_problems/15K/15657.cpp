#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int btr(vector<int> ns, int N, int M, int mi, int nbi, vector<int> ans){
    for(int ni=nbi; ni<N; ni++){
        ans[mi] = ns[ni];

        if(mi < (M-1)) btr(ns, N, M, mi+1, ni, ans);
        else{
            for(auto k: ans) cout << k << ' ';
            cout << '\n';
        }

        ans[mi] = 0;
    }
    return 0;
}

int solve(){
    int N, M;
    cin >> N >> M;

    vector<int> ns(N);
    for(int i=0; i<N; i++) cin >> ns[i];
    sort(ns.begin(), ns.end());

    vector<int> ans(M, 0);
    btr(ns, N, M, 0, 0, ans);
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}