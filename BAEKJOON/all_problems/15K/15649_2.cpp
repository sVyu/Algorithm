#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solve(){
    int N, M;
    cin >> N >> M;

    vector<int> v(N);
    for(int i=0; i<N; i++) v[i] = i+1;

    do{
        for(int i=0; i< M; i++) cout << v[i] << ' ';
        cout << '\n';
        reverse(v.begin()+M, v.end());
    }while(next_permutation(v.begin(), v.end()));

    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie();
    solve();
    return 0;
}