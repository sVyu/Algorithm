#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
typedef long long ll;

bool cmp(ll a, ll b){
    return a > b;
}

// opreator()는 반대로 해주어야 한다
struct pqcmp {
    bool operator()(ll a, ll b){
        return a > b;
    }
};

int solve(){
    int N, M;
    cin >> N >> M;

    vector<ll> ns(N, 0);
    for(int i=0; i<N; i++) cin >> ns[i];

    if(N <= M){
        cout << *max_element(ns.begin(), ns.end());
        return 0;
    }

    sort(ns.begin(), ns.end(), cmp);
    // for(auto n:ns) cout << n << ' '; cout << '\n';

    ll ans = 0;
    priority_queue<ll, vector<ll>, pqcmp> pq;

    int i=0;
    for(; i<M ;i++){
        pq.push(ns[i]);
    }
    while(i<N){
        priority_queue<ll, vector<ll>, pqcmp> new_pq;
        ll min_time = pq.top();
        ans += min_time;

        int new_pq_sz = 0;
        while(!pq.empty()){
            ll t = pq.top(); pq.pop();
            if((t-min_time)>0){
                new_pq.push(t-min_time);
                new_pq_sz++;
            }
        }

        for(int npqi=new_pq_sz; npqi<M and i<N; npqi++){
            new_pq.push(ns[i++]);
        }
        pq = new_pq;
    }

    ll last_val = 0;
    while(!pq.empty()){
        last_val = pq.top(); pq.pop();
    }

    cout << ans+last_val;
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie();
    solve();
    return 0;
}

/*
20 4
1 1 1 1 2 2 2 2 4 4 4 4 8 8 8 8 16 16 16 16
[ans] 31
*/
