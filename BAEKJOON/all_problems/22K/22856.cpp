#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int sz=1e5+1;
vector<vector<int>> g(sz);
int visit_cnt=0;
int move_cnt=0;

void traversal(int n, int v){
    if(g[v][0] != -1){
        traversal(n, g[v][0]);
        move_cnt++;
    }
    ++visit_cnt;
    if(g[v][1] != -1){
        traversal(n, g[v][1]);
        move_cnt++;
    }
    if(visit_cnt == n) return;
    move_cnt++;
}

void solve(){
    int n; cin >> n;
    for(int i=0; i<n; i++){
        int p, l, r; cin >> p >> l >> r;
        g[p] = {l, r};
    }

    traversal(n, 1);
    cout << move_cnt;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}