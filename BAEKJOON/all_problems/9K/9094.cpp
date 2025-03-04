#include <bits/stdc++.h>
using namespace std;

int main(void){
    int t; cin >> t;
    while(t--){
        int cnt = 0;

        int n, m; cin >> n >> m;
        for(int a=1; a<=(n-2); ++a){
            for(int b=a+1; b<=(n-1); ++b){
                if(((a*a)+(b*b)+m)%(a*b) == 0) cnt++;
            }
        }

        cout << cnt << '\n';
    }
}