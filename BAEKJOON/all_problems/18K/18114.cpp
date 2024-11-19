#include <bits/stdc++.h>
#define ll long long
// typedef long long ll;
using namespace std;

void solve(){
    int n, c; cin >> n >> c;
    vector<int> ws(n); for(auto &w:ws) cin >> w;
    sort(ws.begin(), ws.end());

    if(find(ws.begin(), ws.end(), c) != ws.end()){
        cout << 1;
        return;
    }

    for(int i=0; i<(n-1); ++i){
        int l=i+1, r=n-1;
        while(l <= r){
            int mid=(l+r)/2;
            int val = ws[i]+ws[mid];

            if(val == c){
                cout << 1;
                return;
            }
            else if(val < c)    l = mid+1;
            else                r = mid-1;
        }
    }

    for(int i=0; i<(n-2); ++i){
        int l=i+1, r=n-1;
        while(l < r){
            ll val = ws[i]+ws[l]+ws[r];
            if(val == c){
                cout << 1;
                return;
            }
            else if(val < c)    ++l;
            else                --r;
        }
    }
    cout << 0;
}

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}
