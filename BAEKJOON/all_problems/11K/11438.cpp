#include <bits/stdc++.h>
using namespace std;

void init_dfs(int parent, int v, vector<vector<int>>& g, vector<int>& parents, vector<int>& lvs, int lv){
    lvs[v] = lv;
    for(auto u:g[v]){
        if(u == parent) continue;
        parents[u] = v;
        init_dfs(v, u, g, parents, lvs, lv+1);
    }
}

int up(vector<vector<int>>& st, int v, int gap){
    int lg_gap = int(log2(gap));
    for(int i=lg_gap; i>=0; --i){
        if((1 << i) & gap){
            v = st[i][v];
        }
    }
    return v;
}

void solve(){
    int n; cin >> n;

    int mx = n+1;
    vector<vector<int>> g(mx);
    for(int i=1; i<n; ++i){ // n-1 times
        int a, b; cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }

    vector<int> parents(mx, -1);
    vector<int> lvs(mx, -1);
    init_dfs(0, 1, g, parents, lvs, 0);

    // init sparse_table
    int k = int(log2(*max_element(lvs.begin(), lvs.end()))); // log 2 max_lv
    vector<vector<int>> st(k+1, vector<int>(mx, -1));
    for(int j=1; j<=n; ++j) st[0][j] = parents[j];
    for(int i=1; i<=k; ++i)
        for(int j=1; j<=n; ++j){
            if(st[i-1][j] == -1) continue;
            st[i][j] = st[i-1][st[i-1][j]];
        }

    int m; cin >> m;
    while(m--){
        int a, b; cin >> a >> b;
        if(lvs[a] > lvs[b]) a = up(st, a, lvs[a]-lvs[b]);
        if(lvs[a] < lvs[b]) b = up(st, b, lvs[b]-lvs[a]);

        if(a == b){
            cout << a << '\n';
        }
        else{
            int k = int(log2(lvs[a]));
            for(int i=k; i>=0; --i){
                if(st[i][a] != st[i][b]){
                    a = st[i][a];
                    b = st[i][b];
                }
            }
            cout << st[0][a] << '\n';
        }
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}


/*
    original code + debugging
*/
// #include <bits/stdc++.h>
// using namespace std;

// void init_dfs(int parent, int v, vector<vector<int>>& g, vector<int>& parents, vector<int>& lvs, int lv){
//     lvs[v] = lv;
//     for(auto u:g[v]){
//         if(u == parent) continue;
//         parents[u] = v;
//         init_dfs(v, u, g, parents, lvs, lv+1);
//     }
// }

// int up(vector<vector<int>>& st, int v, int gap){
//     int lg_gap = int(log2(gap));
//     // cout << "gap : " << gap << '\n';
//     // cout << "lg_gap : " << lg_gap << '\n';
//     // cout << "(pre) v : " << v << '\n';
//     for(int i=lg_gap; i>=0; --i){
//     // for(int i=0; i<=lg_gap; ++i){
//         // int t = 1 << i; // target <- up_cnt
//         if((1 << i) & gap){
//             // cout << "i : " << i << '\n';
//             // cout << "v : " << v << '\n';
//             v = st[i][v];
//         }
//     }
//     // cout << "(post) v : " << v << '\n';
//     return v;
// }

// void solve(){
//     int n; cin >> n;

//     int mx = n+1;
//     vector<vector<int>> g(mx);
//     // vector<vector<int>> g(mx, vector<int>());
//     for(int i=1; i<n; ++i){ // n-1 times
//         int a, b; cin >> a >> b;
//         g[a].push_back(b);
//         g[b].push_back(a);
//     }

//     vector<int> parents(mx, -1);
//     vector<int> lvs(mx, -1);
//     init_dfs(0, 1, g, parents, lvs, 0);

//     // cout << "\n------------------------------\n";
//     // for(auto k:parents) cout << k << ' ';
//     // cout << '\n';
//     // for(auto k:lvs) cout << k << ' ';
//     // cout << "\n------------------------------\n";
//     // cout << parents[1] << ' ' << lvs[1] << '\n';

//     // init sparse_table
//     int k = int(log2(*max_element(lvs.begin(), lvs.end()))); // log 2 max_lv
//     vector<vector<int>> st(k+1, vector<int>(mx, -1));
//     for(int j=1; j<=n; ++j) st[0][j] = parents[j];
//     for(int i=1; i<=k; ++i)
//         for(int j=1; j<=n; ++j){
//             if(st[i-1][j] == -1) continue;
//             st[i][j] = st[i-1][st[i-1][j]];
//         }

//     // for(auto r:st){
//     //     for(auto el:r) cout << el << ' ';
//     //     cout << '\n';
//     // }
//     // cout << "------------------------------\n";

//     int m; cin >> m;
//     while(m--){
//         int a, b; cin >> a >> b;
//         if(lvs[a] > lvs[b]) a = up(st, a, lvs[a]-lvs[b]);
//         if(lvs[a] < lvs[b]) b = up(st, b, lvs[b]-lvs[a]);

//         if(a == b){
//             cout << a << '\n';
//         }
//         else{
//             int k = int(log2(lvs[a]));
//             for(int i=(k-1); i>=0; --i){
//                 // int upped_a = st[i][a];
//                 // int upped_a = up(st, a, 1 << i);
//                 // int upped_b = st[i][b];
//                 if(st[i][a] != st[i][b]){
//                     a = st[i][a];
//                     b = st[i][b];
//                 }
//             }
//             cout << st[0][a] << '\n';
//         }
//     }
// }

// int main(void){
//     ios::sync_with_stdio(0);
//     cin.tie(0);
//     solve();
//     return 0;
// }