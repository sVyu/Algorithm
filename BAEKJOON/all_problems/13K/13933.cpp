#include <iostream>
#include <vector>
using namespace std;

int pos_check(vector<int> ws, int tg){
    bool pos = true;
    int pre = -1;

    for(auto w:ws){
        if(w <= tg) continue;
        else if(w == pre) pre = -1;
        else{ // w != pre
            if(pre == -1) pre = w;
            else{
                pos = false;
                break;
            }
        }
    }

    if(pre != -1) pos = false;      //
    return pos;
}

int solve(){
    int n; cin >> n;
    int sz = 2*n;
    vector<vector<int>> ws(2, vector<int>(n, 0));

    for(int x=0; x<2; x++)
        for(int y=0; y<n; y++)
            cin >> ws[x][y];
    // for(auto w:ws) cout << w << ' ';

    int lo=0, hi=1e9;
    int ans=-1;

    while(lo <= hi){
        int mid = (lo+hi)/2;
        bool pos = pos_check(ws[0], mid) & pos_check(ws[1], mid);

        if(pos){
            ans = mid;
            hi = mid-1;
        }else{
            lo = mid+1;
        }
    }

    cout << ans;
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    solve();
    return 0;
}