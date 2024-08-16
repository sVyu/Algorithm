// 2024/08/16 17:11 ~ 17:52
// 중복 조합은 next_permutation, prev_permutation 활용 AC가 안 그려진다

#include <iostream>
#include <vector>
// #include <algorithm>
using namespace std;

int btr(int N, int M, int mi, int bn, vector<int>& ans){
    for(int n=bn; n<=N; n++){
        ans[mi] = n;

        if(mi < (M-1))  btr(N, M, mi+1, n, ans);
        else{
            for(auto k:ans) cout << k << ' ';
            cout << '\n';
        }

        ans[mi] = 0;
    }
    return 0;
}

int solve(){
    int N, M;
    cin >> N >> M;

    vector<int> ans(M, 0);
    btr(N, M, 0, 1, ans);

    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}