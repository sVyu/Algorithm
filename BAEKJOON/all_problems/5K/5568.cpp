#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, k; cin >> n >> k;

    vector<int> zs(n); for(auto &z:zs) cin >> z;
    sort(zs.begin(), zs.end());

    vector<int> bits(n, 0);
    for(int i=(n-1); i>=(n-k); i--) bits[i] = 1;

    set<string> set_string;

    do{
        vector<int> zs2;
        for(int i=0; i<n; i++) if(bits[i]) zs2.push_back(zs[i]);

        do{
            string tmp="";
            for(auto z:zs2) tmp += to_string(z);
            set_string.insert(tmp);
        }while(next_permutation(zs2.begin(), zs2.end()));
    }while(next_permutation(bits.begin(), bits.end()));

    cout << set_string.size();
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}