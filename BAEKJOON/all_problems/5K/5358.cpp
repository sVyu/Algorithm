#include <bits/stdc++.h>
using namespace std;

void solve(){
    string s;
    getline(cin, s);

    while(!cin.eof()){
        for(auto c:s){
            if(c == 'e')        cout << 'i';
            else if(c == 'i')   cout << 'e';
            else if(c == 'E')   cout << 'I';
            else if(c == 'I' )  cout << 'E';
            else                cout << c;
        }
        cout << endl;
        getline(cin, s);
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}