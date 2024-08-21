#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int solve(){
    int n; cin >> n;
    vector<vector<ll>> vvbox(n);
    for(int i=0; i<n; i++){
        vector<ll> vbox(3, 0);
        for(int j=0; j<3; j++) cin >> vbox[j];
        sort(vbox.begin(), vbox.end());
        vvbox[i] = vbox;
    }

    int m; cin >> m;
    while(m--){
        ll min_val = LLONG_MAX;
        vector<ll> t(3, 0);
        for(int i=0; i<3; i++) cin >> t[i];
        sort(t.begin(), t.end());

        for(auto vbox: vvbox){
            bool pos = true;
            ll box_area = 1;

            for(int i=0; i<3; i++){
                if(t[i] > vbox[i]) pos = false; 
                else box_area *= vbox[i];
            }

            if(pos) min_val = min(min_val, box_area);
        }

        if(min_val == LLONG_MAX) cout << "Item does not fit." << '\n';
        else cout << min_val << '\n';
    }

    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}