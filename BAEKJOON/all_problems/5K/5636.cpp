#include <bits/stdc++.h>
using namespace std;

const int sz=1e5;
bool sieves[sz];

void solve(){
    fill(sieves, sieves+sz, true);
    for(int i=2; i<sz; i++){
        if(sieves[i]){
            for(int j=2*i; j<sz; j+=i){
                sieves[j]=false;
            }
        }
    }

    string s; cin >> s;
    while(s != "0"){
        int len_s = s.size();
        int max_val = 0;
        for(int k=5; k>0; k--){                 //
            for(int i=0; i<=len_s-k; i++){      // 5-len_s...
                int n = stoll(s.substr(i, k));
                if(sieves[n]) max_val = max(max_val, n);
            }
            if(max_val){
                cout << max_val << '\n';
                break;
            }
        }
        cin >> s;
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}