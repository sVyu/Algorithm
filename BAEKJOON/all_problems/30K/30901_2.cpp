#include <bits/stdc++.h>
using namespace std;

void solve(){
    vector<string> schs(7);
    for(auto &s:schs) cin >> s;

    int d, h; cin >> d >> h;
    int max_tot_cnt = 0;

    vector<int> bits(7, 0);
    for(int i=0; i<d; i++) bits[6-i] = 1;

    do{
        vector<int> targets;
        for(int i=0; i<7; i++) if(bits[i]) targets.push_back(i);

        vector<int> cnts(24, 0);
        for(int i=0; i<d; i++){
            for(int j=0; j<24; j++){
                if(schs[targets[i]][j] == '.') cnts[j] += 1; // targets[i]
            }
        }
        sort(cnts.begin(), cnts.end(), greater<int>());
        max_tot_cnt = max(max_tot_cnt, accumulate(cnts.begin(), cnts.begin()+h, 0));
    }while(next_permutation(bits.begin(), bits.end()));

    cout.precision(10);
    cout << (double)max_tot_cnt/(d*h);
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}