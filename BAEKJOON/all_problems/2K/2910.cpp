#include <bits/stdc++.h>
using namespace std;
#define pp pair<int, oc>

struct oc{
    int order=INT_MAX;
    int cnt=0;

    // bool operator < (const oc _oc) const{
    //     if(cnt == _oc.cnt) return order < _oc.order;
    //     else return cnt < _oc.cnt;
    // };
};

bool cmp(const pp& a, const pp& b){
    if(a.second.cnt == b.second.cnt) return a.second.order < b.second.order;
    else return a.second.cnt > b.second.cnt;
};

void solve(){
    int n, c; cin >> n >> c;
    map<int, oc> voc;

    for(int i=0; i<n; i++){
        int k; cin >> k;
        voc[k].order = min(voc[k].order, i);
        voc[k].cnt++;
    }

    vector<pp> vpp(voc.begin(), voc.end());
    sort(vpp.begin(), vpp.end(), cmp);

    for(auto _pp:vpp){
        for(int i=0; i<_pp.second.cnt; i++) cout << _pp.first << ' ';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}