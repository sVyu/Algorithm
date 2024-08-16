// 2024/08/16 14:49 ~ 14:59

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#define pp pair<string, int>
using namespace std;

bool cmp(pp& a, pp&b){
    if(a.second != b.second){
        return a.second > b.second;
    }else if(a.first.length() != b.first.length()){
        return a.first.length() > b.first.length();
    }else{
        return a.first.compare(b.first) < 0;
    }
}

int solve(){
    int N, M;
    cin >> N >> M;

    map<string, int> m;
    while(N--){
        string s; cin >> s;
        if(s.length() < M) continue;
        m[s]++;
    }

    vector<pp> vec(m.begin(), m.end());
    sort(vec.begin(), vec.end(), cmp);

    for(auto a:vec) cout << a.first << '\n';
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}