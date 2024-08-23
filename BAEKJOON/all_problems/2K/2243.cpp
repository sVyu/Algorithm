#include <bits/stdc++.h>
using namespace std;

const int sz = 1e6+1;
int a[sz];
int tree[4*sz];

// int init(int s, int e, int node){
//     if(s == e) tree[node] = a[sz];
//     int mid = (s+e)/2;
//     return tree[node] = init(s,mid,node*2)+init(mid+1,e,node*2+1);
// }

int sum_cnt(int s, int e, int node, int l, int r){
    if(r < s || e < l) return 0;
    else if(l <= s && e <= r) return tree[node];
    int mid = (s+e)/2;
    return sum_cnt(s, mid, node*2, l, r)+sum_cnt(mid+1, e, node*2+1, l, r);
}

int update(int s, int e, int node, int i, int diff){
    if(i < s || e < i) return 0;    // !(s <= i && i <= e)
    tree[node] += diff;
    if(s == e) return 0;
    int mid = (s+e)/2;
    update(s, mid, node*2, i, diff);
    update(mid+1, e, node*2+1, i, diff);
    return 0;
}

int solve(){
    int n; cin >> n;
    while(n--){
        int cmd; cin >> cmd;
        if(cmd == 2){
            int i, diff; cin >> i >> diff;
            update(0, sz-1, 1, i, diff);
        }else{
            int target; cin >> target;

            // binary_search
            int lo = 1, hi = 1e6;
            int ti = -1; // target_idx;

            while(lo <= hi){
                int mid = (lo+hi)/2;
                if(sum_cnt(0, sz-1, 1, 1, mid) >= target){
                    ti = mid;
                    hi = mid-1;
                } else{
                    lo = mid+1;
                }
            }

            cout << ti << '\n';
            update(0, sz-1, 1, ti, -1);
        }
    }
    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}