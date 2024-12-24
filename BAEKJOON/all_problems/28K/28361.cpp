#include <bits/stdc++.h>
using namespace std;

int main(void){
    int n; cin >> n;
    cout << n << '\n';

    if(n%3 == 2){
        cout << 1 << ' ';
        int k = 2;
        while(k < n){
            cout << k << ' ' << k+2 << ' ' << k+1 << ' ';
            k += 3;
        }
        cout << k << ' ' << 1;
    }else{
        int k = 1;
        while(k < n){
            cout << k << ' ' << k+2 << ' ' << k+1 << ' ';
            k += 3;
        }
        if(k==n) cout << k << ' ';
        cout << 1;
    }

    return 0;
}