// Ã¹ cpp queue + stack È°¿ë -> AC ~

#include <iostream>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

int solve(){
    int N; cin >> N;
    vector<int> A(N);
    for(int i=0; i<N; i++) cin >> A[i];
    vector<int> ns(N);
    for(int i=0; i<N; i++) cin >> ns[i];

    stack<int> s;
    for(int i=0; i<N; i++){
        if(!A[i]) s.push(ns[i]);
    }
    queue<int> q;
    while(!s.empty()){
        q.push(s.top());
        s.pop();
    }

    int M; cin >> M;
    while(M--){
        int val; cin >> val;
        q.push(val);
        cout << q.front() << ' ';
        q.pop();
    }

    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}