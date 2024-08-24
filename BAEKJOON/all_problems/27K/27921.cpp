#include <bits/stdc++.h>
using namespace std;

int solve(){
    // 입력값 받기
    int h1, w1;
    cin >> h1 >> w1;
    char board1[h1][w1];
    for(int i=0; i<h1; i++) for(int j=0; j<w1; j++) cin >> board1[i][j];

    int h2, w2;
    cin >> h2 >> w2;
    char board2[h2][w2];
    for(int i=0; i<h2; i++) for(int j=0; j<w2; j++) cin >> board2[i][j];

    /*
        ans 선언 및 초기화
        요구에 따라 최소 개수를 구해야 하기 때문에 min 으로 값을 줄여가며 갱신해야 하므로
        초기값은 가장 큰 값 (모든 동전을 옮겨야 하는 경우 → 모든 동전의 개수)
    */
    int all_coins_cnt=0;
    for(int i=0; i<h1; i++) for(int j=0; j<w1; j++) if(board1[i][j] == 'O') all_coins_cnt++;
    int ans = all_coins_cnt;

    // sx: standard x (기준점 x)
    // board1 - 2중 for문
    for(int sx1=0; sx1<h1; sx1++){
        for(int sy1=0; sy1<w1; sy1++){
            // board2 - 2중 for문 (총 4중 for문)
            for(int sx2=0; sx2<h2; sx2++){
                for(int sy2=0; sy2<w2; sy2++){
                    // 기준점들을 바탕으로 최대한의 공통 넓이만큼 동전 위치 비교 및 ans 갱신
                    int rx = min(h1-1-sx1, h2-1-sx2);
                    int ry = min(w1-1-sy1, w2-1-sy2);
                    // cout << rx << ' ' << ry << '\n';

                    int same_position_coin_cnt = 0;
                    // 6중 for문 - TLE? NO
                    for(int tx=0; tx<=rx; tx++){
                        for(int ty=0; ty<=ry; ty++){
                            if(board1[sx1+tx][sy1+ty] == 'O' and
                                board1[sx1+tx][sy1+ty] == board2[sx2+tx][sy2+ty]
                            )
                            same_position_coin_cnt++;
                        }
                    }

                    ans = min(ans, all_coins_cnt - same_position_coin_cnt);
                }
            }
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