// 이 코드는 왜 통과가 안 되지?
#include <bits/stdc++.h>
using namespace std;


void solve(){
    int n; cin >> n;
    int sz = 1e6+1;
    bool check[sz]={0};

    while(n--){
        string s; cin >> s;
        if(s[0] == '-') continue;

        try{s.substr(6, 1);}
        catch(exception e){
            check[stoi(s)]=true;
        }
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
    cout.tie(0);
    solve();
    return 0;
}