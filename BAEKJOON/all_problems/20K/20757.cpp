#include <bits/stdc++.h>
using namespace std;

// find_parent
int fp(vector<int>& parent, int x){
    if(parent[x] != x){
        parent[x] = fp(parent, parent[x]);
    }
    return parent[x];
}

// union_parent
int up(vector<int>& parent, int a, int b){
    int pa = fp(parent, a);
    int pb = fp(parent, b);

    if(pa > pb) parent[a] = pb;
    else        parent[b] = pa;
    return 0;
}

int solve(){
    int T; cin >> T;
    while(T--){
        int N; cin >> N;
        // vector<vector<int>> board(N, vector<int>(N,0));
        vector<int> parent(N, 0);
        for(int i=0; i<N; i++) parent[i]=i;

        for(int x=0; x<N; x++){
            for(int y=0; y<N; y++){
                int road; cin >> road;
                if(x == y) continue;
                if(road and fp(parent, x) != fp(parent, y)){
                    up(parent, x, y);
                }
            }
        }

        set<int> set_p;
        for(auto p:parent) set_p.insert(p);
        cout << N-set_p.size() << '\n';
    }
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}