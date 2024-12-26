#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    while(n--){
        string s; cin >> s;
        int n = s.size();
        vector<int> cnts(8, 0);

        for(int i=2; i<n; ++i){
            string t = s.substr(i-2, 3);
            if(t == "TTT")      ++cnts[0];
            else if(t == "TTH") ++cnts[1];
            else if(t == "THT") ++cnts[2];
            else if(t == "THH") ++cnts[3];
            else if(t == "HTT") ++cnts[4];
            else if(t == "HTH") ++cnts[5];
            else if(t == "HHT") ++cnts[6];
            else                ++cnts[7];
        }
        for(auto c:cnts) cout << c << ' ';
        cout << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}