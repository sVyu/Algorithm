// 2024.09.04 12:42 ~ 01:05
#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, d, k, c;
    cin >> n >> d >> k >> c;

    vector<int> zs(2*n);
    for(int i=0; i<n; i++){
        int z; cin >> z;
        zs[i]= z;
        zs[n+i] = z;
    }

    int cnt = 0;
    int cv = 0;
    int bowls[d+1]={0};
    for(int i=0; i<k; i++){
        if(!bowls[zs[i]]) cnt++;
        bowls[zs[i]]++;
    }

    int l=0, r=k-1;
    if(!bowls[c]) cv=1;
    int ans = cnt+cv;

    while(n--){
        if(bowls[zs[l]] == 1) cnt--;        //
        bowls[zs[l++]]--;
        if(!bowls[zs[++r]]) cnt++;
        bowls[zs[r]]++;

        if(!bowls[c]) cv=1;
        else cv =0;                         //
        ans = max(ans, cnt+cv);
    }
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}