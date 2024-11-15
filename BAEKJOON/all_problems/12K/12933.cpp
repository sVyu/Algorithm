#include <bits/stdc++.h>
using namespace std;

void solve(){
    string s; cin >> s;
    vector<int> cnts(5, 0);
    int max_cnt_duck = 0;
    int cnt_duck = 0;

    for(auto c:s){
        if(c == 'q'){
            ++cnts[0];
            max_cnt_duck = max(max_cnt_duck, ++cnt_duck);
        }
        else if(c == 'u'){
            if(cnts[0]-- <= 0){
                cout << -1;
                return;
            }
            ++cnts[1];
        }
        else if(c == 'a'){
            if(cnts[1]-- <= 0){
                cout << -1;
                return;
            }
            ++cnts[2];
        }
        else if(c == 'c'){
            if(cnts[2]-- <= 0){
                cout << -1;
                return;
            }
            ++cnts[3];
        }
        else{
            if(cnts[3]-- <= 0){
                cout << -1;
                return;
            }
            --cnt_duck;
        }
    }

    if(cnt_duck){
        cout << -1;
        return;
    }

    cout << max_cnt_duck;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}