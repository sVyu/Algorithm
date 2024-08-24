#include <bits/stdc++.h>
using namespace std;

// key point: (a+b+c == d) == (a+b == d-c)
int solve(){
    int n; cin >> n;
    if(n == 1){
        cout << 0;
        return 0;
    }

    int ns[n];
    for(int i=0; i<n; i++) cin >> ns[i];

    int ans = 0;
    int sz = 4e5+1;         // size, -200,000 ~ 200,000
    int cv = 2e5;           // correction_value
    bool cache[sz] = {0};
    cache[ns[0]*2+cv] = true;

    for(int i=1; i<n; i++){
        // a+b == d-c
        for(int j=0; j<i; j++){         // less
            if(cache[ns[i]-ns[j]+cv]){
                ans++;
                break;
            }
        }

        // add new a+b
        for(int j=0; j<=i; j++){        // need equal
            cache[ns[i]+ns[j]+cv] = true;
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