#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool palindrome_check(string s, int sz){
    for(int l=0,r=sz-1; l<r; l+=1,r-=1)
        if(s[l] != s[r]) return false;
    return true;
}

int solve(){
    int n; cin >> n;
    while(n--){
        int bn; cin >> bn;

        string sn = to_string(bn);
        string left_sn = sn.substr(0, 3);
        string right_sn = left_sn;
        reverse(right_sn.begin(), right_sn.end());
        int tn = stoi(left_sn+right_sn);

        int gap = abs(tn-bn);
        for(int delta=0; delta<=gap; delta+=1){
            if(palindrome_check(to_string(bn-delta), 6)){
                cout << (bn-delta) << '\n';
                break;
            }
            if(palindrome_check(to_string(bn+delta), 6)){
                cout << (bn+delta) << '\n';
                break;
            }
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