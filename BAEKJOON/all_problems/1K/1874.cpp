#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    stack<int> s;
    string ans = "";
    int now = 1;

    while(n--){
        int k; cin >> k;
        if(now <= k){
            while(now <= k){
                s.push(now++);
                ans += '+';
            }
        } else {
            if(!(!s.empty() and s.top() == k)){
                cout << "NO";
                return;
            }
        }
        ans += '-';
        s.pop();
    }

    for(auto c:ans){
        cout << c << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}