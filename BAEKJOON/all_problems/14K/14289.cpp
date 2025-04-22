#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

vector<vector<ll>> mul(vector<vector<ll>> a, vector<vector<ll>> b, int n, ll mod){
    vector<vector<ll>> res(n, vector<ll>(n, 0));
    for(int x=0; x<n; ++x){
        for(int y=0; y<n; ++y){
            for(int k=0; k<n; ++k){
                res[x][y] = (res[x][y] + a[x][k]*b[k][y]) % mod;
            }
        }
    }
    return res;
}

// divide_and_conquer
vector<vector<ll>> dac(vector<vector<ll>> g, int d, int n, ll mod){
    if(d == 1) return g;
    if(d % 2){
        return mul(g, dac(g, d-1, n, mod), n, mod);
    }else{
        vector<vector<ll>> half_mul_g = dac(g, d/2, n, mod);
        return mul(half_mul_g, half_mul_g, n, mod);
    }
}

void solve(){
    ll n, m; cin >> n >> m;
    vector<vector<ll>> g(n, vector<ll>(n, 0));

    for(ll i=0; i<m; ++i){
        int a, b; cin >> a >> b;
        --a; --b;
        ++g[a][b];
        ++g[b][a];
    }

    ll d; cin >> d;
    ll mod = ll(1e9)+7LL;

    // vector<vector<ll>> res = dac(g, d, n, mod);
    cout << dac(g, d, n, mod)[0][0];
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}