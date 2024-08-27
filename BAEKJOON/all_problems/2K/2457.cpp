#include <bits/stdc++.h>
using namespace std;

bool cmp(vector<int> a, vector<int> b){
    if(a[0] != b[0])    return a[0] < b[0];
    else                return a[1] <= b[1];
}

int solve(){
    int n; cin >> n;
    vector<vector<int>> pds(n, vector<int>(4, 0));
    for(int x=0; x<n; x++) for(int y=0; y<4; y++) cin >> pds[x][y];
    // sort(pds.begin(), pds.end(), cmp);   // Runtime Error: Segfault
    stable_sort(pds.begin(), pds.end(), cmp);

    vector<int> now = {3, 1};
    for(int i=0, cnt=1; i<n; cnt++){
        bool renew = false;
        vector<int> max_date = now;         // now ~ max_date

        while(i<n){
            vector<int> pd_start = {pds[i][0], pds[i][1]};
            vector<int> pd_end = {pds[i][2], pds[i][3]};
            if(cmp(pd_start, now)){
                renew = true;
                if(cmp(max_date, pd_end)) max_date = pd_end;
                i++;
            }
            else break;
        }
        if(!renew) break;
        if(cmp({12, 1}, max_date)){
            cout << cnt;
            return 0;
        }
        now = max_date;
    }

    cout << 0;
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}