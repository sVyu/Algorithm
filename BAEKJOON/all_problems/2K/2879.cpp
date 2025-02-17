// O(N) 풀이
#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n; cin >> n;
    vector<int> zs(n);         for(auto &z:zs) cin >> z;
    vector<int> targets(n);    for(auto &t:targets) cin >> t;
    vector<int> gaps(n);
    for(int i=0; i<n; ++i) gaps[i] = zs[i]-targets[i];

    int abs_base = 0;
    int sign = gaps[0];
    int max_abs_gap_in_area = abs(gaps[0]);
    int ans = 0;

    for(int gap:gaps){
        int abs_gap = abs(gap);
        if(sign == 0 and gap != 0) sign = gap;

        // 양수*음수 혹은 음수*양수
        if(sign*gap < 0){
            ans += max_abs_gap_in_area-abs_base;
            max_abs_gap_in_area = abs_gap;
            abs_base = 0;
            sign = gap;
            // cout << "[1] " << i << ' ' << abs_gap <<  ' ' << ans << '\n';
            continue;
        }
        
        // 같은 부호 구간이지만 절대값이 낮아질 때
        if(max_abs_gap_in_area > abs_gap){
            ans += max_abs_gap_in_area-abs_base;
            max_abs_gap_in_area = abs_gap;
            abs_base = abs_gap;
            continue;
        }
        
        max_abs_gap_in_area = abs_gap;

        // else if((sign> 0 and max_abs_gap_in_area > gap)){
        //     ans += max_abs_gap_in_area-abs_base;
        //     max_abs_gap_in_area = abs(gap);
        //     abs_base = gap;
        // }
        // else if(sign<0 and max_abs_gap_in_area > abs(gap)){
        //     ans += max_abs_gap_in_area-abs_base; // abs_base : 음수
        //     max_abs_gap_in_area = abs(gap);
        //     abs_base = abs(gap);
        // }
    }

    ans += max_abs_gap_in_area-abs_base;
    cout << ans;

}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}