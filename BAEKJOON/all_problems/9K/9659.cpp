#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

/*
1 sk -- 1
2 cy
3 sk -- 3
4 cy
5 sk -- 3 1 1
6 cy
7 sk
8 
*/

int main(void){
    ll n; cin >> n;
    string s = "SK";
    if(n%2 == 0) s = "CY";

    cout << s;
    return 0;
}