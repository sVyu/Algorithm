#include <iostream>
#include <set>
#include <string>
using namespace std;

int solve(){
    int N; cin >> N;
    set<string> dancers = {"ChongChong"};

    while(N--){
        string s1, s2;
        cin >> s1 >> s2;

        if(dancers.count(s1)) dancers.insert(s2);
        if(dancers.count(s2)) dancers.insert(s1);
    }

    cout << dancers.size();
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}