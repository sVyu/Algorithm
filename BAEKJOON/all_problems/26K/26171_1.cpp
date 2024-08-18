// first cpp interactive problem

#include <iostream>
using namespace std;

int solve(){
    int n=100;
    int ans=0;

    for(int x=1; x<=n; x++){
        for(int y=1; y<=n; y++){
            cout << "? " << x << ' ' << y << '\n';
            cout << flush;
            string s; cin >> s;
            if(s.compare("ArrayIndexOutOfBoundsException") == 0){
                n = y-1;
                continue;
            }
            ans = max(ans, stoi(s));
        }
    }

    cout << "! " << ans << '\n';
    cout << flush;
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}