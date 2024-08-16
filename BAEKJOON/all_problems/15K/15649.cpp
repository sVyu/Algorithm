// 2024/08/16 15:25 ~ 15:43 (local env clear) ~ 15:54 (debug completed -> boj platform clear)
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int btr(vector<vector<int>> &seqs, vector<int>& seq, int N, int M, int mi, bool selected[]){
    for(int k=1; k<=N; k++){
        if(!selected[k]){
            selected[k] = true;
            seq.push_back(k);

            if(mi < (M-1))  btr(seqs, seq, N, M, mi+1, selected);
            else            seqs.push_back(seq);

            selected[k] = false;
            seq.pop_back();
        }
    }
    return 0;
}

int solve(){
    int N, M;
    cin >> N >> M;

    bool selected[N+1];                             //
    fill(&selected[0], &selected[0]+(N+1), false);  //

    // sequence
    vector<vector<int>> seqs;
    vector<int> seq;
    btr(seqs, seq, N, M, 0, selected);

    for(auto seq:seqs){
        for(auto n:seq) cout << n << ' '; 
        cout << '\n';
    }
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie();
    solve();
    return 0;
}