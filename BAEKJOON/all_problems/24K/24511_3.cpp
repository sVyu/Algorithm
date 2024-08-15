// Ã¹ deque È°¿ë -> AC ~

#include <iostream>
#include <vector>
#include <deque>
using namespace std;

int solve(){
    int N; cin >> N;
    vector<int> A(N);
    for(int i=0; i<N; i++) cin >> A[i];
    vector<int> ns(N);
    for(int i=0; i<N; i++) cin >> ns[i];

    deque<int> d;
    for(int i=0; i<N; i++){
        if(!A[i]) d.push_front(ns[i]);
    }
    // deque<int>::iterator it;
    // for(it = d.begin(); it != d.end(); ++it){
    //     cout << *it << ' ';
    // }

    int M; cin >> M;
    while(M--){
        int val; cin >> val;
        d.push_back(val);
        cout << d.front() << ' ';
        d.pop_front();
    }

    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}