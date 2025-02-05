#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, p, w, l, g;
    cin >> n >> p >> w >> l >> g;

    set<string> can_win_names;
    while(p--){
        string name, wl; cin >> name >> wl;
        if(wl == "W") can_win_names.insert(name);
    }

    int score = 0;
    for(int i=0; i<n; ++i){
        string name; cin >> name;
        if(can_win_names.count(name))   score += w;
        else                            score = max(0, score-l);

        if(score >= g){
            cout << "I AM NOT IRONMAN!!";
            return;
        }
    }

    cout << "I AM IRONMAN!!";
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}