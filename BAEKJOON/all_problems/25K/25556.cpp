#include <bits/stdc++.h>
using namespace std;

int solve(){
    int vector_stack_size = 4;
    vector<stack<int>> vs(vector_stack_size, stack<int>({0}));
    bool pos = true;

    int N; cin >> N;
    while(N--){
        int item; cin >> item;
        int ti = -1, max_val = -1;
        for(int i=0; i<vector_stack_size; i++){
            if(max_val < vs[i].top() and vs[i].top() < item){
                ti = i;
                max_val = vs[i].top();
            }
        }
        if(ti == -1){
            pos = false;
            break;
        }
        vs[ti].push(item);
    }

    if(pos) cout << "YES";
    else    cout << "NO";
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}