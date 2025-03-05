#include <bits/stdc++.h>
using namespace std;

void solve(){
    string s1, s2;
    cin >> s1 >> s2;

    string s3;
    int sz = s1.size();
    // cout << sz;

    for(int i=0; i<sz; ++i){
        int val = (s2[i]-s1[i]);
        if(val <= 0) val += 26;
        s3 += 'A'+(val-1);
    }
    // cout << s3 << '\n';

    // bool checks[sz+1];
    // for(int i=0; i<=sz; ++i) checks[i] = true;
    // for(int i=2; i<=sz; ++i){
    //     if(checks[i]){
    //         for(int j=2*i; j<=sz; j+=i) checks[j] = false;
    //     }
    // }

    for(int min_len=1; min_len<=sz; ++min_len){
        if(sz%min_len) continue;
        bool pos = true;
        for(int i=0; i<sz; ++i){
            if(s3[i] != s3[i%min_len]){
                pos = false;
                break;
            }
        }

        if(pos){
            cout << string(s3.begin(), s3.begin()+min_len) << '\n';
            return;
        }
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}