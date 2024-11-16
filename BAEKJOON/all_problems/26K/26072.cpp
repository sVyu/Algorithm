#include <bits/stdc++.h>
using namespace std;

int main(void){
    cout << fixed;
    cout.precision(10);

    int n, l; cin >> n >> l;
    vector<int> xs(n); for(auto &x:xs) cin >> x;
    vector<int> ws(n); for(auto &w:ws) cin >> w;

    double lo=0, hi=l;
    while((hi-lo) > 1e-10){
        double mid = (lo+hi)/2;
        double val = 0;

        for(int i=0; i<n; ++i){
            if(xs[i] < mid) val -= ws[i]*(mid-xs[i]);
            else            val += ws[i]*(xs[i]-mid);
        }

        if(val > 0)     lo = mid;
        else            hi = mid;
        // cout << lo << ' ' << hi << '\n';
    }

    cout << (hi+lo)/2;
}