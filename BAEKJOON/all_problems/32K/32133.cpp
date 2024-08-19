#include <bits/stdc++.h>
using namespace std;

int solve(){
    int N, M, K;
    cin >> N >> M >> K;
    K -= 1;

    map<char, char> rsp_map{{'R', 'S'}, {'S', 'P'}, {'P', 'R'}};
    vector<string> vals(N);
    for(int i=0; i<N; i++) cin >> vals[i];

    int ans_len = 51;
    string ans_str = "";

    for(int i=0; i<N; i++){
        string now_str = "";
        set<int> pos_idxs;
        for(int idx=0; idx<N; idx++) pos_idxs.insert(idx);
        pos_idxs.erase(i);
        int sum_pos_idxs = N-1;

        for(int j=0; j<M; j++){
            set<int> new_pos_idxs = pos_idxs;
            now_str.push_back(vals[i][j]);
            for(auto pi: pos_idxs){
                if(vals[i][j] != vals[pi][j]){
                    new_pos_idxs.erase(pi);
                    sum_pos_idxs -= 1;
                }
            }
            pos_idxs = new_pos_idxs;
            if(sum_pos_idxs <= K){
                if(ans_len > (j+1)){
                    ans_len = (j+1);
                    ans_str = now_str;
                }
                break;
            }
        }
    }

    if(ans_len == 51) cout << -1;
    else{
        cout << ans_len << '\n';
        for(auto c:ans_str) cout << rsp_map[c];
    }

    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}