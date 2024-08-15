#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int solve(){
    int N; cin >> N;

    priority_queue<int, vector<int>, greater<int>> pq;
    int n;
    for(int i=0; i<N; i++){
        cin >> n;
        pq.push(n);
    }

    for(int i=0; i<(N*(N-1)); i++){
        cin >> n;
        if(n > pq.top()){
            pq.push(n);
            pq.pop();
        }
    }

    cout << pq.top();
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}