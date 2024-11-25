#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct ch {
    ll c;
    ll h;
};

bool cmp1(ch a, ch b){
    return a.c < b.c;
}

bool cmp2(ch a, ch b){
    return a.h > b.h;
}

void solve(){
    int tc; cin >> tc;
    while(tc--){
        int n, k; cin >> n >> k;

        vector<ll> cs(n); for(auto &c:cs) cin >> c;
        vector<ll> hs(n); for(auto &h:hs) cin >> h;
        vector<ch> chs(n);
        for(int i=0; i<n; i++) chs[i] = {cs[i], hs[i]};
        sort(chs.begin(), chs.end(), cmp1);

        int tv = chs[k-1].c;    // target_value
        int ti;                 // target_idx
        for(ti = n-1; ti >= 0; --ti){
            if(chs[ti].c == tv) break; 
        }

        // ll sum_h = 0LL;
        // priority_queue<ll> pq;
        // for(int i=0; i<=ti; ++i) pq.push(chs[i].h);
        // while(k--){
        //     sum_h += pq.top(); pq.pop();
        // }

        ll sum_h = 0;
        sort(chs.begin(), chs.begin()+ti+1, cmp2);
        for(auto el:vector<ch>(chs.begin(), chs.begin()+k)){
            sum_h += el.h;
        }

        cout << tv << ' ' << sum_h << '\n';
    }
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

// struct ch {
//     ll c;
//     ll h;

//     bool operator < (const ch _ch) const{
//         if(c != _ch.c) return c < _ch.c;
//         return h > _ch.h;
//     }
// };

// void solve(){
//     int tc; cin >> tc;
//     while(tc--){
//         int n, k; cin >> n >> k;

//         vector<ll> cs(n); for(auto &c:cs) cin >> c;
//         vector<ll> hs(n); for(auto &h:hs) cin >> h;
//         vector<ch> chs(n);
//         for(int i=0; i<n; i++) chs[i] = {cs[i], hs[i]};
//         stable_sort(chs.begin(), chs.end());

//         ll max_c = 0, sum_h = 0;
//         for(auto el:vector<ch>(chs.begin(), chs.begin()+k)){
//             max_c = max(max_c, el.c);
//             sum_h += el.h;
//         }
//         cout << max_c << ' ' << sum_h;
//     }
// }

// int main(void){
//     ios::sync_with_stdio(0);
//     cin.tie(0);
//     solve();
//     return 0;
// }