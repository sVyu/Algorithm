#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solve(){
    int N, M;
    cin >> N >> M;

    int sz = M*N;
    vector<int> ns(sz);
    for(int i=0; i<N; i++){
        int n; cin >> n;
        for(int j=0; j<M; j++) ns[M*i+j] = n;
    }
    sort(ns.begin(), ns.end());     //

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