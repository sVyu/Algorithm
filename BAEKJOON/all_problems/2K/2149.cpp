#include <bits/stdc++.h>
using namespace std;

struct ic{
    int idx;
    char ch;

    bool operator < (const ic _ic){
        if(ch != _ic.ch) return (ch-'A') < (_ic.ch-'A');
        return idx < _ic.idx;
    }
};

struct ii{
    int idx1;
    int idx2;

    bool operator < (const ii _ii){
        return idx1 < _ii.idx1;
    }
};

void solve(){
    string key; cin >> key;
    string ss; cin >> ss;

    int len_key = key.length();
    int repeat_cnt = ss.length()/len_key;

    vector<ic> ics(len_key);
    for(int i=0; i<len_key; ++i){
        ics[i] = {i, key[i]};
    }
    sort(ics.begin(), ics.end());

    vector<vector<char>> board(repeat_cnt, vector<char>(len_key));
    int num=0;
    for(int i=0; i<repeat_cnt; ++i){
        for(int j=0; j<len_key; ++j){
            board[num%repeat_cnt][num/repeat_cnt] = ss[len_key*i+j];
            num++;
            // cout << num%repeat_cnt << ' ' << num/repeat_cnt << '\n';
        }
    }

    vector<ii> iis(len_key);
    for(int i=0; i<len_key; ++i) iis[i] = {ics[i].idx, i};
    sort(iis.begin(), iis.end());

    for(int i=0; i<repeat_cnt; ++i){
        for(int j=0; j<len_key; ++j){
            cout << board[i][iis[j].idx2];
        }
    }

}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}