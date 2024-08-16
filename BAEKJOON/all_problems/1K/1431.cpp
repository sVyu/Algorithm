// 2024/08/16 15:04 ~ 15:14

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(string a, string b){
    if(a.length() != b.length()) return a.length() < b.length();

    int suma=0, sumb=0;
    for(auto c:a) if('0' <= c and c <= '9') suma += c-'0';
    for(auto c:b) if('0' <= c and c <= '9') sumb += c-'0';

    if(suma != sumb)    return suma < sumb;
    else                return a.compare(b) < 0;
}

int solve(){
    int N; cin >> N;

    vector<string> ss(N);
    for(int i=0; i<N; i++) cin >> ss[i];

    sort(ss.begin(), ss.end(), cmp);
    for(auto s:ss) cout << s << '\n';

    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}