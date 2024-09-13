#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct coins{
    char a;
    int n;
};

void solve(){
    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        queue<coins> q;
        for(int i=0; i<n; i++){
            char a; int val;
            cin >> a >> val;
            q.push({a, val});
        }

        stack<coins> s;
        while(!q.empty()){
            auto [a, val] = q.front(); q.pop();
            if(!s.empty() and s.top().a == a){
                val += s.top().n; s.pop();
            }
            if(val%3) s.push({a, val%3});
            if(val/3) q.push({a, val/3});
        }

        ll ans = 0;
        while(!s.empty()){
            ans += s.top().n; s.pop();
        }
        cout << ans << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}