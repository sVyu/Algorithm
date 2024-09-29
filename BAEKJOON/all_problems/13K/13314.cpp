#include <bits/stdc++.h>
using namespace std;

void solve(){
    int N = 100;

    cout << N << '\n';
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            if(i==j) cout << "0 ";
            else if(j==N) cout << "1\n";
            else if(i==N) cout << "1 ";
            else cout << "100 ";
        }
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}