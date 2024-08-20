#include <bits/stdc++.h>
using namespace std;

bool pos = false;

int btr(string s, int len_s, string t, int len_t){
    if(len_s == len_t){
        if(s.compare(t) == 0) pos = true;
        return 0;
    }

    if(t[0] == 'B'){
        string new_t = t.substr(1, len_t);
        reverse(new_t.begin(), new_t.end());
        btr(s, len_s, new_t, len_t-1);
    }
    if(t[len_t-1] == 'A'){
        btr(s, len_s, t.substr(0, len_t-1), len_t-1); //
    }
    return 0;
}

int solve(){
    string s, t;
    cin >> s >> t;

    btr(s, s.length(), t, t.length());
    cout << pos;

    return 0;
}

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(0);
    solve();
    return 0;
}