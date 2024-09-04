// 2024.09.04. 17:34 ~ 17:51
// ans, overflow
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// struct cmp{
//     bool operator()(int a, int b){
//         return a > b;
//     }
// };

void solve(){
    int t; cin >> t;
    while(t--){
        int k; cin >> k;
        // priority_queue<int, vector<int>, cmp> pq;
        priority_queue<ll, vector<ll>, greater<ll>> pq;
        for(int i=0; i<k; i++){
            ll z; cin >> z;
            pq.push(z);
        }

        ll ans=0; //
        for(int i=0; i<k-1; i++){
            ll sum=0;
            for(int j=0; j<2; j++){
                sum += pq.top();
                pq.pop();
            }
            ans += sum;
            pq.push(sum);
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