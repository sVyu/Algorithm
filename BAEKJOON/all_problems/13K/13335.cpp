#include <bits/stdc++.h>
using namespace std;

struct at{
    int a;
    int t;
};

void solve(){
    int n, w, l; cin >> n >> w >> l;
    vector<int> zs(n); for(auto &z:zs) cin >> z;
    queue<at> q;

    int cap = 0, time = 0;
    for(int i=0; i<n; i++){
        int a = zs[i];
        time += 1;

        while(!q.empty() and ((cap+a) > l)){
            auto [ta, tt] = q.front(); q.pop();
            cap -= ta;
            time += max(w-(time-tt), 0);    //
        }

        cap += a;
        q.push({a, time});
    }

    while(!q.empty()){
        auto [ta, tt] = q.front(); q.pop();
        time += max(w-(time-tt), 0);
    }

    cout << time;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}