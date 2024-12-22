#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct dot{
    int x;
    int y;
};

ll cal_dist(dot a, dot b){
    auto [x1, y1] = a;
    auto [x2, y2] = b;
    return pow(x1-x2,2)+pow(y1-y2,2);
}

void solve(){
    vector<dot> dots(3);
    for(auto &dot:dots){int x, y; cin >> x >> y; dot = {10*x,10*y};}

    // right isosceles triangle, 직각이등변삼각형
    map<ll, vector<int>> dmap;
    vector<vector<int>> vidxs = {{0, 1}, {0, 2}, {1, 2}};
    for(auto idxs:vidxs){
        int i = idxs[0], j = idxs[1];

        ll d = cal_dist(dots[i], dots[j]);
        if(dmap.count(d))   dmap.erase(d);
        else                dmap[d] = {i, j};
    }

    // find target dot's index
    vector<bool> ts(3, true);
    for(auto [_, idxs]:dmap){
        for(auto i:idxs) ts[i] = false;
    }
    int ti = find(ts.begin(), ts.end(), true)-ts.begin();

    // 직각이등변삼각형 밑변의 중심점 구하기
    dot center={0, 0};
    for(auto [_, idxs]:dmap){
        for(auto i:idxs){
            auto [x, y] = dots[i];
            center.x += x;
            center.y += y;
        }
    }

    // center.x /2 *2
    cout << (center.x-dots[ti].x)/10 << ' ' << (center.y-dots[ti].y)/10;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}