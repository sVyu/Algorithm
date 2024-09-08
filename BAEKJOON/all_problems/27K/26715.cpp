#include <bits/stdc++.h>
using namespace std;

void solve(){
    string s, target; cin >> s >> target;
    if(s == target){
        cout << 1;
        return;
    }

    set<string> set_s={s};
    int t=1;
    while(++t){
        int cnts[10]{};
        for(auto c:s) cnts[c-'0']++;

        string ns="";
        for(int i=0; i<10; i++){
            if(cnts[i]){
                ns += to_string(cnts[i]*10+i);
            }
        }

        if(ns == target){
            if(t < 100) cout << t;
            else        cout << "I'm bored .";
            return;
        }

        s=ns;
        if(set_s.count(s)) break;
        set_s.insert(s);
    }
    cout << "Does not appear";
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}