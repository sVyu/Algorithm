#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    vector<int> sieve(n+1, true);
    vector<int> colors(n+1, 0);
    colors[1]=1;

    int k=2;
    for(int i=2; i<=n; i++){
        if(sieve[i]){
            for(int j=i; j<=n; j+=i){
                sieve[j] = false;
                colors[j] = k;
            }
            k++;
        }
    }

    cout << --k << '\n';
    for(auto c:vector<int>(colors.begin()+1, colors.end())) cout << c << ' ';
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}