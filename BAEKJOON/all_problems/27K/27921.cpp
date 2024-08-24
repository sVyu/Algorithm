#include <bits/stdc++.h>
using namespace std;

int solve(){
    // �Է°� �ޱ�
    int h1, w1;
    cin >> h1 >> w1;
    char board1[h1][w1];
    for(int i=0; i<h1; i++) for(int j=0; j<w1; j++) cin >> board1[i][j];

    int h2, w2;
    cin >> h2 >> w2;
    char board2[h2][w2];
    for(int i=0; i<h2; i++) for(int j=0; j<w2; j++) cin >> board2[i][j];

    /*
        ans ���� �� �ʱ�ȭ
        �䱸�� ���� �ּ� ������ ���ؾ� �ϱ� ������ min ���� ���� �ٿ����� �����ؾ� �ϹǷ�
        �ʱⰪ�� ���� ū �� (��� ������ �Űܾ� �ϴ� ��� �� ��� ������ ����)
    */
    int all_coins_cnt=0;
    for(int i=0; i<h1; i++) for(int j=0; j<w1; j++) if(board1[i][j] == 'O') all_coins_cnt++;
    int ans = all_coins_cnt;

    // sx: standard x (������ x)
    // board1 - 2�� for��
    for(int sx1=0; sx1<h1; sx1++){
        for(int sy1=0; sy1<w1; sy1++){
            // board2 - 2�� for�� (�� 4�� for��)
            for(int sx2=0; sx2<h2; sx2++){
                for(int sy2=0; sy2<w2; sy2++){
                    // ���������� �������� �ִ����� ���� ���̸�ŭ ���� ��ġ �� �� ans ����
                    int rx = min(h1-1-sx1, h2-1-sx2);
                    int ry = min(w1-1-sy1, w2-1-sy2);
                    // cout << rx << ' ' << ry << '\n';

                    int same_position_coin_cnt = 0;
                    // 6�� for�� - TLE? NO
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