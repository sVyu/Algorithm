#include <bits/stdc++.h>
using namespace std;

int solve(){
    int n; cin >> n;

    int sz = 0;
    vector<int> nums(sz, 0);
    while(n--){
        int k; cin >> k;

        vector<int> new_nums(sz*2+1, 0);
        for(int i=0; i<sz; i++){
            new_nums[i] = nums[i];
        }
        for(int i=sz; i<2*sz; i++){
            new_nums[i] = nums[i-sz]+k;
        }
        sz = 2*sz+1;
        new_nums[sz-1] = k;
        nums = new_nums;
    }

    sz = 2e6+1;
    bool check[sz];
    fill(check, check+sz, false);
    for(auto num:nums) check[num]=true;

    for(int i=1; i<sz; i++){
        if(!check[i]){
            cout << i;
            break;
        }
    }

    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}