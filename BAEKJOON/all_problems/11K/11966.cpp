#include <iostream>
using namespace std;
typedef long long ll;

int main(void){
    ll n; cin >> n;
    while(n > 1){
        if(n % 2){
            cout << 0;
            return 0;
        }
        n /= 2;
    }
    cout << 1;
    return 0;
}