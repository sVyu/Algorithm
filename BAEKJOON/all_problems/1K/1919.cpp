#include <bits/stdc++.h>
using namespace std;

int main(void){
    string s1, s2;
    cin >> s1 >> s2;

    vector<int> alphas1(26, 0), alphas2(26, 0);
    for(auto a:s1) alphas1[a-97] += 1;
    for(auto a:s2) alphas2[a-97] += 1;

    int ans = 0;
    for(int i=0; i<26; i++){
        ans += abs(alphas1[i]-alphas2[i]);
    }
    cout << ans;

    return 0;
}