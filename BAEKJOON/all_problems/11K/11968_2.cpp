#include <bits/stdc++.h>
using namespace std;

int main(void){
    int N;
    cin >> N;
    int idx_limit = 2*N+1;
    vector<bool> bessie_turns(idx_limit, true);

    int ti;
    for(int i=0; i<N; i++){
        cin >> ti;
        bessie_turns[ti] = false;
    }

    int ans = 0;
    int lower_elsie_cards = 0;
    for(int i=1; i<idx_limit; i++){
        if(not bessie_turns[i]){
            lower_elsie_cards++;
            continue;
        }
        if(lower_elsie_cards>0){
            lower_elsie_cards--;
            ans++;
        }
    }

    cout << ans;
}