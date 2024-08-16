#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// bool cmp(int a, int b){
//     return a > b;
// }

int solve(){
    int N, M;
    cin >> N >> M;

    vector<int> ns(N);
    for(int i=0; i<N; i++) ns[i] = i+1;

    vector<bool> bs(N, false);
    for(int i=0; i<M; i++) bs[i] = true;
    // sort(bs.begin(), bs.end(), cmp);

    do{
        for(int i=0; i<N; i++){
            if(bs[i]) cout << ns[i] << ' ';
        }
        cout << '\n';
    }while(prev_permutation(bs.begin(), bs.end()));

    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie();
    solve();
    return 0;
}