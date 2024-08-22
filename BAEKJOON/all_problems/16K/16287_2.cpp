#include <bits/stdc++.h>
#define pp pair<int, int>
using namespace std;

const int sz = 8e5;
int nums[5000];
int dpsz[sz];
pp dp[sz][3];

int solve(){
    int w, n;
    cin >> w >> n;

    // vector<int> nums(n);
    for(int i=0; i<n; i++) cin >> nums[i];

    for(int i=0; i<n-1; i++){
        for(int j=i+1; j<n; j++){
            int sum_val = nums[i]+nums[j];
            if(dpsz[sum_val] >= 3) continue;
            dp[sum_val][dpsz[sum_val]] = {i, j};
            dpsz[sum_val]++;
        }
    }

    for(int i=2; i<=(w/2); i++){
        int j = w-i;

        if((dpsz[i] >= 3 and dpsz[j]) or (dpsz[i] and dpsz[j] >= 3)){
            cout << "YES";
            return 0;
        }

        for(int ti=0; ti<dpsz[i]; ti++){
            for(int tj=0; tj<dpsz[j]; tj++){
                pp pp1 = dp[i][ti], pp2 = dp[j][tj];

                if(pp1.first != pp2.first and pp1.first != pp2.second and
                    pp1.second != pp2.first and pp1.second != pp2.second){
                        cout << "YES";
                        return 0;
                }
            }
        }
    }

    cout << "NO";
    return 0;
}

int main(void){
    ios::sync_with_stdio;
    cin.tie(0);
    solve();
    return 0;
}