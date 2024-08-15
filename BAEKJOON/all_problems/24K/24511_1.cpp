// 첫 cpp queue 활용 코드 -> TLE ㅎㅎㅎ

// #include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int solve(){
    int N; cin >> N;
    vector<int> A(N);
    for(int i=0; i<N; i++) cin >> A[i];
    vector<int> ns(N);
    for(int i=0; i<N; i++) cin >> ns[i];

    int cnt_queue = 0;
    for(auto a:A) cnt_queue += !a;
    // cout << cnt_queue;

    vector<queue<int>> vq(cnt_queue, queue<int>());
    int vqi = 0;
    for(int i=0; i<N; i++){
        if(!A[i]){
            vq[vqi].push(ns[i]);
            vqi += 1;
        }
    }

    int M; cin >> M;
    for(int i=0; i<M; i++){
        int input_val; cin >> input_val;
        int output_val = input_val;
        for(int i=0; i<cnt_queue; i++){
            vq[i].push(input_val);
            input_val = output_val = vq[i].front();
            vq[i].pop();
        }
        cout << output_val << ' ';
    }

    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}