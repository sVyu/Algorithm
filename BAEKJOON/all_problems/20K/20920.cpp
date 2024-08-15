#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
# define pp pair<string, int>
using namespace std;

bool cmp(const pp& a, const pp& b){
    if(a.second != b. second){
        return a.second > b.second;
    } else if (a.first.length() != b.first.length()){
        return a.first.length() > b.first.length();
    } else {
        return a.first.compare(b.first) < 0; // here 
    }
}

int solve(){
    int N, M;
    cin >> N >> M;

    map<string, int> m;
    for(int i=0; i<N; i++){
        string word; cin >> word;
        if(word.length() < M) continue;
        m[word]++;
    }

    // map<string, int>::iterator it;
    // for(auto it = m.begin(); it != m.end(); it++){
    //     cout << it->first << ' ' << it->second << '\n';
    // }

    vector<pp> vec(m.begin(), m.end());
    sort(vec.begin(), vec.end(), cmp);

    // for(const auto& p:vec){
    for(auto p:vec){
        cout << p.first << '\n';
    }

    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}