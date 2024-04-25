#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        string s1, s2;
        cin >> s1 >> s2;

        vector<int> arr1(26, 0), arr2(26, 0);
        for(auto a:s1) arr1[a-97] += 1;
        for(auto a:s2) arr2[a-97] += 1;

        bool pos = true;
        for(int i=0; i<26; i++){
            if(arr1[i] != arr2[i]){
                cout << "Impossible" << "\n";
                pos = false;
                break;
            }
        }

        if(pos) cout << "Possible" << "\n";
    }

    return 0;
}