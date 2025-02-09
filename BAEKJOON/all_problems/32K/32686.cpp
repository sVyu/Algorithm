#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

double cal_damage(ll r, ll a, ll d, ll time){
    ll quo = time/(r+a);
    double ans = quo*d;

    ll res_time = max(0LL, time-quo*(r+a)-r);
    ans += ((double)res_time/a)*d;

    return ans;
}

void solve(){
    int n, s, e; cin >> n >> s >> e;

    double ans = 0.0;
    while(n--){
        ll r, a, d; cin >> r >> a >> d;
        ans += cal_damage(r,a,d,e)-cal_damage(r,a,d,s);
    }

    cout.precision(10);
    cout << ans/(e-s);
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}