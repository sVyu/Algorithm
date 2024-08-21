#include <bits/stdc++.h>
using namespace std;

int solve(){
    int n; cin >> n;
    int case_num = 1;
    while(n){
        int tmp;
        for(int i=0; i<n; i++) cin >> tmp;

        cout << "Case " << case_num << ": Sorting... done!" << '\n';
        case_num++;
        cin >> n;
    }
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}