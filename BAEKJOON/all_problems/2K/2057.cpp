#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;

int main(){
    ull n; cin >> n;
    if(n == 0){
        cout << "NO";
        return 0;
    }

    ull sum_val=0, a=1;
    ull limit = ull(1e18);
    for(int i=1; i<=100; i++){
        if(a <= n and n <= (a+sum_val)){
            cout << "YES";
            return 0;
        }

        sum_val += a;
        a *= i;

        if(sum_val > limit){
            break;
        }
    }

    cout << "NO";
    return 0;
}