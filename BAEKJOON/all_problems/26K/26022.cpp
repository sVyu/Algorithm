#include <bits/stdc++.h>
using namespace std;

int gcd(int a, int b){
    if(b == 0) return a;
    return gcd(b, a%b);
}

void solve(){
    int l, w, n; cin >> l >> w >> n;
    if((l*w)%n){
        cout << "impossible";
        return;
    }

    vector<vector<char>> board(l, vector<char>(w, ' '));
    int rect_x = l/gcd(l,n);
    n/=gcd(l,n);
    int rect_y = w/gcd(w,n);

    int quo_x = l/rect_x;
    int quo_y = w/rect_y;

    for(int r=0; r<quo_x; r++){
        for(int c=0; c<quo_y; c++){
            int base_x=r*rect_x;
            int base_y=c*rect_y;

            for(int x=0; x<rect_x; x++){
                for(int y=0; y<rect_y; y++){
                    board[base_x+x][base_y+y] = 'A'+(r*quo_y)+c;
                }
            }
        }
    }

    for(int x=0; x<l; x++){
        for(int y=0; y<w; y++) cout << board[x][y];
        cout << '\n';
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}