#include <bits/stdc++.h>
using namespace std;
const int sz = 4e4;

void solve(){
    vector<bool> check(sz, true);
    vector<int> nums(3001, 0);

    int cnt = 0;
    for(int i=2; i<sz; i++){
        if(check[i]){
            int k=0;
            for(int j=i+1; j<sz; j++){
                if(check[j]){
                    if(++k == i){
                        check[j] = false;
                        k = 0;
                    }
                }
            }
            nums[++cnt] = i;
            if(cnt == 3000) break;
        }
    }

    int n; cin >> n;
    while(n){
        cout << nums[n] << '\n';
        cin >> n;
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}