// AC
#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    int sz = 1e6+1;
    bool check[sz]={0};

    while(n--){
        string s; cin >> s;
        if(s[0] == '-') continue;
        if(s.length() >= 7) continue;
        check[stoi(s)] = true;
    }

    for(int i=0; i<sz; i++){
        if(!check[i]){
            cout << i;
            break;
        }
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}