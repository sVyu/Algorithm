#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solve(){
    int N; cin >> N;
    int sz = N*N;
    vector<int> ns(sz, 0);
    for(int i=0; i<sz; i++) cin >> ns[i];
    // for(auto n:ns) cout << n << ' ';

    sort(ns.begin(), ns.end());
    cout << ns[sz-N];
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}