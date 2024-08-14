#include <bits/stdc++.h>
using namespace std;

int main(void){
    int n;
    cin >> n;

    vector<int> switchs(n+1, 0);
    for(int i=1; i<=n; i++)  cin >> switchs[i];

    int k;
    cin >> k;

    int gender, val;
    for(int c=0; c<k; c++){
        cin >> gender >> val;
        if(gender == 1){
            for(int i=val; i<=n; i+=val){
                switchs[i] = (switchs[i]+1)%2;
            }
        }else{
            switchs[val] = (switchs[val]+1)%2;

            int l = val-1, r = val+1;
            while ((l > 0) and (r <= n) and (switchs[l] == switchs[r])){
                switchs[l] = (switchs[l]+1)%2;
                switchs[r] = (switchs[r]+1)%2;
                l -= 1;
                r += 1;
            }
        }
    }

    for(int i=1; i<=n; i++){
        cout << switchs[i] << ' ';
        if(i % 20 == 0) cout << '\n';
    }
}