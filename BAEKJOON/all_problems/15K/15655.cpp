#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solve(){
    int N, M;
    cin >> N >> M;

    vector<int> ns(N);
    for(int i=0; i<N; i++) cin >> ns[i];
    sort(ns.begin(), ns.end());

    vector<bool> bs(N, false);
    for(int i=0; i<M; i++) bs[i]=true;

    do{
        for(int i=0; i<N; i++) if(bs[i]) cout << ns[i] << ' ';
        cout << '\n';
    }while(prev_permutation(bs.begin(), bs.end()));

    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}