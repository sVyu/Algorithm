#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// vector<string>>
// less<>(), greater<>()
// 문제 이해 실수 1 단순히 한 행당 점 개수 카운트 해서 sort
// max, min
// 문제 이해 실수 2 각 자리마다 점 개수 카운트 해서 sort..
//    → for j, for i, for k 돌면서 각 자리마다 연속해서 체크할 때 확률 최대값을 모아서 또 최대값
// 문제 이해 실수 3 날짜 안 이어서 해도 됨, 그렇게 해야 함
// 시간복잡도 계산 24C12 -> 2704156

// ll f(ll a){
//     ll n=1;
//     for(int k=2; k<=a; k++) n*=k;
//     return n;
// }

// ll c(ll a, ll b){
//     ll n = 1;
//     for(ll k=a; k>(a-b); k--) n*= k;
//     return n/f(b);
// }

// cout << c(3,2) << '\n';
// cout << c(3,1) << '\n';
// cout << c(24,12) << '\n';

// TLE,,
void solve(){
    vector<string> schs(7, string());
    for(auto &sch: schs) cin >> sch;

    int d, h; cin >> d >> h;
    double max_prob = 0;

    vector<int> idxs(24, 0);
    for(int i=0; i<24; i++) idxs[i] = i;
    vector<int> bits(24, 0);
    for(int i=0; i<h; i++) bits[23-i]=1;

    do{
        vector<int> cnts(7, 0);
        vector<int> targets(h, 0);
        int ti=0;
        for(int j=0; j<24; j++) if(bits[j]) targets[ti++] = j;

        for(int i=0; i<7; i++){
            for(auto t:targets){
                if(schs[i][t] == '.') cnts[i]++;
            }
        }

        sort(cnts.begin(), cnts.end(), greater<int>());
        // int tot = 0;
        // for(int i=0; i<d; i++) tot += cnts[i];
        int tot = accumulate(cnts.begin(), cnts.begin()+d, 0);
        max_prob = max(max_prob, (double)tot/(d*h));

    }while(next_permutation(bits.begin(), bits.end()));

    cout.precision(10);
    cout << max_prob;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}