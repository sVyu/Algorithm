#include <bits/stdc++.h>
using namespace std;

bool can_be_time(int a, int b){
    if(a < 24 and b < 60) return true;
    return false;
}

int dates[13] = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
bool can_be_date(int a, int b){
    if(a == 0 | a > 12 | b == 0) return false;  // b == 0
    if(dates[a] >= b) return true;
    return false;
}

void solve(){
    int t; cin >> t;
    while(t--){
        int a, b; cin >> a >> b;
        if(can_be_time(a, b))   cout << "Yes ";
        else                    cout << "No ";

        if(can_be_date(a, b))   cout << "Yes\n";
        else                    cout << "No\n";
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}