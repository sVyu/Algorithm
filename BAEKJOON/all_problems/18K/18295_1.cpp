// AC
#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    set<string> ss;

    while(n--){
        string s; cin >> s;
        ss.insert(s);
    }

    for(int i=0; i<=(1e6+1); i++){
        if(!ss.count(to_string(i))){
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