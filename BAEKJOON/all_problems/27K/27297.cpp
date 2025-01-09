/*
1 4
1
1
1
10000
*/

/*
1 3
-3
-4
-4
*/

/*
1 3
3
4
4
*/

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int n, m; cin >> n >> m;
    vector<vector<ll>> dots(m, vector<ll>(n));
    for(auto &r:dots) for(auto &el:r) cin >> el;

    vector<ll> ans(n);
    for(int y=0; y<n; ++y){
        vector<ll> zs(m);
        for(int x=0; x<m; ++x) zs[x] = dots[x][y];
        sort(zs.begin(), zs.end());

        if(m%2) ans[y]=zs[m/2];
        else    ans[y]=(zs[m/2]+zs[(m/2)-1])/2;
    }

    ll tot = 0;
    for(int x=0; x<m; ++x)
        for(int y=0; y<n; ++y) tot += abs(dots[x][y]-ans[y]);
    cout << tot << '\n';
    for(auto k:ans) cout << k << ' ';
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}


// #include <bits/stdc++.h>
// using namespace std;
// typedef long long ll;

// void solve(){
//     int n, m; cin >> n >> m;
//     vector<vector<ll>> dots(m, vector<ll>(n));
//     for(auto &r:dots) for(auto &el:r) cin >> el;

//     vector<ll> ans(n);
//     for(int y=0; y<n; ++y){
//         ll sum = 0;
//         for(int x=0; x<m; ++x) sum += dots[x][y];

//         ll tmp_val = sum/m;
//         ll shortest_dist = LLONG_MAX;
//         for(auto val:{tmp_val-1, tmp_val, tmp_val+1}){
//             ll dist = 0;
//             for(int x=0; x<m; ++x) dist += abs(val-dots[x][y]);
//             if(shortest_dist > dist){
//                 shortest_dist = dist;
//                 ans[y] = val;
//             }
//         }
//     }

//     ll tot = 0;
//     for(int x=0; x<m; ++x)
//         for(int y=0; y<n; ++y) tot += abs(dots[x][y]-ans[y]);
//     cout << tot << '\n';
//     for(auto k:ans) cout << k << ' ';
// }

// int main(void){
//     ios::sync_with_stdio(0);
//     cin.tie(0);
//     solve();
//     return 0;
// }