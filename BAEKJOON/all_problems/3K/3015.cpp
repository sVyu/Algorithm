/*
edge case 0
5
4
2
2
1
2
*/
/*
edge case 1
1
1
*/

#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    int ans = 0;
    stack<int> s;
    int len_stack = 0;
    int h = -1;
    int pre_h = -1;
    int low_val_cnt = 0;

    while(n--){
        cin >> h;
        if(!s.empty()){
            if(s.top()<h){
                while(!s.empty() && s.top()<h){
                    ans += 1;
                    s.pop();
                    len_stack -= 1;
                }
            }
        }

        s.push(h);
        len_stack += 1;

        if(pre_h == h){
            ans += low_val_cnt;
            low_val_cnt += 1;
        }else{
            low_val_cnt = 1;
        }

        pre_h = h;
        if(len_stack > low_val_cnt)
            ans += 1;

        cout << "hmm " << h << ", " << ans << ", " << len_stack << ", " << low_val_cnt << '\n';
    }
    cout << ans << '\n';

    return 0;
}
