#include <bits/stdc++.h>
using namespace std;

void solve(){
    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        bool visited[n+1];
        fill(visited, visited+n+1, false);
        visited[0] = true;

        vector<int> cnts(n+1, -1);
        for(int i=1; i<=n; ++i){
            int k; cin >> k;
            cnts[i] = k;
        }

        int ans[n+1] = {0, };

        bool pos = true;
        for(int i=n; i>=1; --i){
            int cnt = -1;
            int val = -1;

            for(int j=1; j<=n; ++j){
                if(visited[j]) continue;
                ++cnt;
                if(cnt == cnts[i]){
                    val = j;
                    break;
                }
            }

            if(val != -1){
                ans[i] = val;
                visited[val] = true;
            }else{
                pos = false;
                break;
            }
        }

        if(pos){
            for(int i=1; i<=n; ++i) cout << ans[i] << ' ';
            cout << '\n';
            continue;
        }
        cout << "IMPOSSIBLE\n";
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}