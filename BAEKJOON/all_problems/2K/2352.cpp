#include <bits/stdc++.h>
using namespace std;

int binarySearch(vector<int> &lis, int left, int right, int target){
    int mid;

    while(left < right){
        mid = (left+right)/2;
        if(target > lis[mid])   left = mid+1;
        else                    right = mid;
    }

    return right;
}

void solve(){
    int n; cin >> n;
    vector<int> zs(n, 0); for(auto &z:zs) cin >> z;
    vector<int> lis(n, 0);

    lis[0] = zs[0];
    int max_lis_idx = 0;

    for(int i=1; i<n; i++){
        if(lis[max_lis_idx] < zs[i]){
            lis[++max_lis_idx] = zs[i];
        }else{
            int lis_idx = binarySearch(lis, 0, max_lis_idx, zs[i]);
            lis[lis_idx] = zs[i];
        }
    }

    cout << max_lis_idx+1;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}