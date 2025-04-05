#include <bits/stdc++.h>
using namespace std;

void move_by_ladder(int k, string &s, string ladder){
    for(int i=0; i<(k-1); ++i){
        if(ladder[i] == '-'){
            swap(s[i], s[i+1]);
        }
    }
}

void solve(){
    int k; cin >> k;
    int n; cin >> n;
    string ts; cin >> ts;
    string ladders[n];
    for(auto &ladder:ladders) cin >> ladder;
    // for(auto &ladder:ladders) cout << ladder << '\n';

    int question_mark_index = -1;
    for(int i=0; i<n; ++i){
        if(ladders[i][0] == '?')
            question_mark_index = i;
    }
    // cout << question_mark_index << '\n';

    string bs="";
    for(int i=0; i<k; ++i){
        // bs += "A"+i;       //
        bs += 'A'+i;
    }
    // cout << bs << '\n';

    for(int i=0; i<question_mark_index; ++i){
        move_by_ladder(k, bs, ladders[i]);
    }
    // cout << bs << '\n';

    for(int i=n-1; i>=(question_mark_index+1); --i){
        move_by_ladder(k, ts, ladders[i]);
    }
    // cout << ts << '\n';

    int i = 0;
    string ans = "";
    bool pos = true;

    while(i < (k-1)){
        if(bs[i] == ts[i]){
            ans += '*';
            ++i;
        }else if(bs[i] == ts[i+1] and bs[i+1] == ts[i]){
            ans += '-';
            if(i+1 < (k-1)) ans += '*';
            i += 2;
        }else{
            pos = false;
            break;
        }
    }

    if(!pos){
        for(int i=0; i<(k-1); ++i) cout << 'x';
        return;
    }
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}