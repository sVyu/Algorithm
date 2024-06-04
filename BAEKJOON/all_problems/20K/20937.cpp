#include <bits/stdc++.h>
using namespace std;

int main(void){
    vector<int> cnt(50001, 0);

    int N = 0;
    cin >> N;

    int c = 0;
    for(int i=0; i<N; i++){
        cin >> c;
        cnt[c] += 1;
    }

    cout << *max_element(cnt.begin(), cnt.end()) << '\n';
}