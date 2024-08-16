// 2024/08/16 17:01 ~ 17:08

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solve(){
    int N, M;
    cin >> N >> M;

    int sz = M*N;
    vector<int> ns(sz, 0);
    for(int i=0; i<sz; i++) ns[i] = (i/M)+1;
    // for(auto n:ns) cout << n << ' ';

    do{
        for(int i=0; i<M; i++) cout << ns[i] << ' ';
        cout << '\n';
        reverse(ns.begin()+M, ns.end());
    }while(next_permutation(ns.begin(), ns.end()));

    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}