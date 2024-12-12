#include <bits/stdc++.h>
using namespace std;

void btr(int n, vector<char>& signs, int idx, vector<string>& ans, string s, vector<bool> &alloc){
    if(n < idx){
        ans.push_back(s);
        return;
    }

    for(int val=9; val>=0; val--){
        if(idx == 0){
            alloc[val] = true;
            btr(n, signs, idx+1, ans, s+to_string(val), alloc);
            alloc[val] = false;
        }
        else{
            if(signs[idx-1] == '<' and (s[idx-1]-'0') < val and !alloc[val]){
                alloc[val] = true;
                btr(n, signs, idx+1, ans, s+to_string(val), alloc);
                alloc[val] = false;
            }
            else if(signs[idx-1] == '>' and (s[idx-1]-'0') > val and !alloc[val]){
                alloc[val] = true;
                btr(n, signs, idx+1, ans, s+to_string(val), alloc);
                alloc[val] = false;
            }
        }
    }
}

void solve(){
    int n; cin >> n;
    vector<char> signs(n); for(auto &s:signs) cin >> s;
    vector<bool> alloc(10);

    vector<string> ans;
    btr(n, signs, 0, ans, "", alloc);
    cout << ans[0] << '\n' << ans[ans.size()-1];
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}


// #include <bits/stdc++.h>
// using namespace std;

// void solve(){
//     int n; cin >> n;
//     vector<char> signs(n); for(auto &s:signs) cin >> s;

//     vector<int> zs(10);
//     for(int i=0; i<10; ++i) zs[i] = i;

//     vector<vector<int>> ans;
//     do{
//         vector<int> bits(10, 1);
//         for(int i=0; i<=n; ++i) bits[i] = 0; // n+1 °³
//         do{
//             vector<int> ts;
//             for(int k=0; k<10; ++k) if(bits[k] == 0) ts.push_back(k);
//             bool pos = true;

//             for(int k=0; k<n; ++k){
//                 if(bits[k] == '<' and bits[k] > bits[k+1]){
//                     pos = false;
//                     break;
//                 }
//                 if(bits[k] == '>' and bits[k] < bits[k+1]){
//                     pos = false;
//                     break;
//                 }
//             }
//             if(pos) ans.push_back(ts);
//         }while(next_permutation(bits.begin(), bits.end()));
//     }while(next_permutation(zs.begin(), zs.end()));

//     for(auto an:ans){
//         for(auto k:an) cout << k << ' ';
//         cout << '\n';
//     }
// }

// int main(void){
//     ios::sync_with_stdio(0);
//     cin.tie(0);
//     solve();
//     return 0;
// }