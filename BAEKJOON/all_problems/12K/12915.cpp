#include <bits/stdc++.h>
using namespace std;

void solve(){
    int e, em, m, mh, h;
    cin >> e >> em >> m >> mh >> h;

    int lo=0, hi=int(2e5); // 1e5 -> 2e5
    int ans=-1;

    while(lo <= hi){
        int mid = (lo+hi)/2;
        int te=e, tem=em, tm=m, tmh=mh, th=h;
        int tgap = -1;

        // e
        if((te+tem)<mid){
            hi = mid-1;
            continue;
        }
        tgap = (te+tem)-mid;
        tgap = min(tem, tgap);
        tm += tgap;

        // m
        if((tm+tmh)<mid){
            hi = mid-1;
            continue;
        }
        tgap = (tm+tmh)-mid;
        tgap = min(tmh, tgap);
        th += tgap;

        // h
        if(th<mid){
            hi = mid-1;
            continue;
        }

        ans = mid;
        lo = mid+1;
    }
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}