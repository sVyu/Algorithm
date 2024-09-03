// 2024.09.03. 11:26 ~ 
#include <bits/stdc++.h>
using namespace std;

string s="";
bool good_seq(int k){
    for(int i=1; i<=(k/2); i++){    //
        if(s.substr(k-2*i, i) == s.substr(k-i, i)) return false;    //
    }
    return true;
}

bool btr(int i, int n){
    if(i==n){
        if(good_seq(n)) return true;
        else            return false;
    }

    for(int k=1; k<4; k++){
        s += to_string(k);
        if(good_seq(i+1)){
            if(btr(i+1, n)) return true;
            //else            return false; //
        }
        s.pop_back();
    }
    return false;
}

void solve(){
    int n; cin >> n;
    btr(0, n);
    cout << s;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}