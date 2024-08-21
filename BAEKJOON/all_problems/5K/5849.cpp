#include <bits/stdc++.h>
using namespace std;

bool cmp(vector<int>& a, vector<int>& b){
    return a[0] < b[0];
}

int solve(){
    int N; cin >> N;
    vector<vector<int>> vvns(N);
    for(int i=0; i<N; i++){
        vector<int> ns(2);
        for(int j=0; j<2; j++) cin >> ns[j];
        vvns[i] = ns;
    }
    sort(vvns.begin(), vvns.end(), cmp);

    stack<vector<int>> s;
    int max_val = -1e7;

    for(auto vns:vvns){
        if(max_val > vns[1]){
            while(!s.empty() and s.top()[1] > vns[1]){
                s.pop();
            }
        } else {
            max_val = vns[1];
            s.push(vns);
        }
    }

    cout << s.size();
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}