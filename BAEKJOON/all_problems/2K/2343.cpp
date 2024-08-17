#include <iostream>
#include <vector>
using namespace std;

int solve(){
    int N, M;
    cin >> N >> M;

    vector<int> ns(N);
    for(int i=0; i<N; i++) cin >> ns[i];

    int lo=1, hi=1e9;
    int ans = -1;
    while(lo <= hi){
        int mid = (lo+hi)/2;
        int cnt=1, sum=0;

        bool pos=true;
        for(auto n:ns){
            if((sum+n) <= mid){
                sum += n;
            }else{
                if(n > mid){
                    pos=false;
                    break;
                }else{
                    sum = n;
                    cnt++;
                }
            }
        }

        if(cnt <= M and pos){
            ans = mid;
            hi = mid-1;
        }else{
            lo = mid+1;
        }
    }
    cout << ans;
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}