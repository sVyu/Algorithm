// 2024.09.10 11:14 ~ 11:51
#include <bits/stdc++.h>
using namespace std;

// all_permutations
// 각각의 permutation을 탐색으로 체크
// 가능하다면 최소값 갱신

vector<vector<int>> all_permutations(int n){
    vector<vector<int>> all_p;
    for(int one_cnt=1; one_cnt<n; one_cnt++){
        vector<int> base(n, 0);
        for(int j=1; j<=one_cnt; j++) base[n-j]=1;
        do{
            all_p.push_back(base);
        }while(next_permutation(base.begin(), base.end()));
    }
    return all_p;
}

// 탐색
void dfs(vector<int> &p, vector<vector<int>> &g, bool visited[], int v){
    if(!visited[v]){
        visited[v] = true;
        for(auto u:g[v]){
            if(p[v-1] == p[u-1]) dfs(p, g, visited, u);
        }
    }
}

void solve(){
    int n; cin >> n;
    vector<int> zs(n);  for(auto &z:zs) cin >> z;
    vector<vector<int>> g(n+1, vector<int>());
    // vector<vector<int>> g(n+1);
    for(int v=1; v<=n; v++){
        int k; cin >> k;
        for(int i=0; i<k; i++){
            int u; cin >> u;
            g[v].push_back(u);
            g[u].push_back(v);  //
        }
    }

    int ans = 1000;
    vector<vector<int>> all_p = all_permutations(n);
    int sum_zs = accumulate(zs.begin(), zs.end(), 0);
    for(auto p:all_p){
        bool visited[n+1];
        fill(visited, visited+n+1, false);
        bool appeared[2]={false, false};
        for(int v=1; v<=n; v++){
            if(!appeared[p[v-1]]){
                appeared[p[v-1]]=true;
                dfs(p, g, visited, v);
            }
        }

        bool all_visit=true;
        for(int i=1; i<=n; i++) if(!visited[i]) all_visit=false;    //

        if(all_visit){
            int zero_sum = 0;
            for(int i=0; i<n; i++) if(p[i]==0) zero_sum += zs[i];
            ans = min(ans, abs(zero_sum-(sum_zs-zero_sum)));
        }
    }

    // ans = ans == 1000 ? -1: ans;
    if(ans == 1000) ans = -1;
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}