#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int n; cin >> n;
    vector<int> vals(n); for(auto &v:vals) cin >> v;
    vector<int> cnts(n, 1);

    for(int i=0; i<n; i++){
        for(int j=0; j<i; j++){
            if(vals[j] < vals[i] and cnts[j] == cnts[i]){
                cnts[i]++;
            }
        }
    }

    int mx_cnt, m;
    mx_cnt = m = *max_element(cnts.begin(), cnts.end());
    vector<int> ans(mx_cnt, 0);

    for(int i=n-1; i>=0; i--){
        if(cnts[i] == m){
            ans[(m--)-1] = vals[i];
        }
    }

    cout << mx_cnt << '\n';
    for(auto a:ans) cout << a << ' ';
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}