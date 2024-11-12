#include <bits/stdc++.h>
using namespace std;

void solve(){
    string a, b; cin >> a >> b;
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    int sup = 0;
    string ans = "";

    int len_a = a.length();
    int len_b = b.length();
    int n = max(len_a, len_b);

    if(n > len_a){
        int gap = n-len_a;
        while(gap--) a += "0";
    } else if(n > len_b){
        int gap = n-len_b;
        while(gap--) b += "0";
    }

    for(int i=0; i<n; i++){
        int ia = a[i]-'0';
        int ib = b[i]-'0';

        int val = ia+ib+sup;
        ans += to_string(val%10);
        sup = val/10;
    }

    if(sup) ans += to_string(sup);
    reverse(ans.begin(), ans.end());
    cout << ans;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}