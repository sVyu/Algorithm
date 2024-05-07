#include <iostream>
using namespace std;
typedef long long ll;

int main(void){
    ll N = 0;
    double L = 0, W = 0, H = 0;
    double lo = 0.0, hi = 1e9;
    // double moe = 1e-9; // margin of error

    cin >> N >> L >> W >> H;

    // while(abs(hi-lo) >= moe){
    for(int k=0; k<10000; k++){ // Âü°í : https://www.acmicpc.net/board/view/1767
        double mid = (lo+hi)/2;

        ll cnt = (ll)(L/mid)*(ll)(W/mid)*(ll)(H/mid);
        // cout << cnt << '\n';
        // cnt = min(cnt, N);

        if(cnt >= N)lo = mid;
        else hi = mid;
    }
    cout << fixed;
    cout.precision(9);
    cout << abs(lo+hi)/2;

    return 0;
}