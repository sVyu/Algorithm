#include <bits/stdc++.h>
using namespace std;

#define psi pair<string, int>

bool cmp(psi a, psi b){
    return a.first.compare(b.first) < 0;
}

void solve(){
    int n; cin >> n;
    map<string, int> ext_cnts;

    while(n--){
        string s; cin >> s;
        string ext = s.substr(s.find(".")+1);
        ext_cnts[ext]++;
    }

    vector<psi> vpsi(ext_cnts.begin(), ext_cnts.end());
    sort(vpsi.begin(), vpsi.end(), cmp);

    for(auto [ext, cnt]:vpsi){
        cout << ext << ' ' << cnt << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}