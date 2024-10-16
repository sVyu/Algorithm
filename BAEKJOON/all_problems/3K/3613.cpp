#include <bits/stdc++.h>
using namespace std;

void solve(){
    string s; cin >> s;
    int type = 0;

    if(0 <= (s[0]-'A') and (s[0]-'A') <= 25){
        cout << "Error!";
        return;
    }
    if((s[0] == '_')|(s[s.size()-1] == '_')){
        cout << "Error!";
        return;
    }

    for(auto c:s){
        if(c == '_'){
            if(type == 0) type = 1;
            else if(type == 2){
                cout << "Error!";
                return;
            };
        }else if(0 <= (c-'A') and (c-'A') <= 25){
            if(type == 0) type = 2;
            else if(type == 1){
                cout << "Error!";
                return;
            };
        }
    }

    if(type == 0){
        cout << s;
    }else if(type == 1){
        vector<int> idxs;
        int sz = s.size();
        for(int i=0; i<sz; i++) if(s[i]=='_') idxs.push_back(i);
        idxs.push_back(sz);

        int pre_idx = -1;
        for(auto i:idxs){
            if((i-pre_idx) <= 1){
                cout << "Error!";
                return;
            }
            pre_idx=i;
        }

        string ans;
        pre_idx = 0;
        for(auto idx:idxs){
            string t = s.substr(pre_idx, idx-pre_idx);
            t[0] -= 32;
            ans += t;
            pre_idx = idx+1;
        }
        ans[0] += 32;
        cout << ans;
    }else if(type == 2){
        vector<int> idxs;
        int sz = s.size();
        for(int i=0; i<sz; i++){
            if(0 <= (s[i]-'A') and (s[i]-'A') <= 25){
                idxs.push_back(i);
            }
        }
        idxs.push_back(sz);

        string ans;
        int pre_idx = 0;
        for(auto idx:idxs){
            string t = s.substr(pre_idx, idx-pre_idx);
            if(0 <= (t[0]-'A') and (t[0]-'A') <= 25){
                t[0] += 32;
                ans += "_"+t;
            }else{
                ans += t;
            }
            pre_idx = idx;
        }
        cout << ans;
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}