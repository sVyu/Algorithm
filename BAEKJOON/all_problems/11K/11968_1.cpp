#include <iostream>
#include <algorithm>
using namespace std;

bool compare(int a, int b){
    return a<b;
}

int main(void){
    int N = 0;
    cin >> N;

    int elsie_cards[N] = {0};
    int bessie_cards[N] = {0};

    // elsie_cards 값 초기화 (sorted)
    for(int i=0; i<N; i++){
        cin >> elsie_cards[i];
    }
    sort(elsie_cards, elsie_cards+N, compare);

    // bessie_cards 값 초기화 (sorted)
    int elsie_cards_idx = 0;
    int bessie_cards_idx = 0;
    int num_limit = 2*N;
    for(int num=1; num <= num_limit; num++){
        if(elsie_cards_idx < N and num == elsie_cards[elsie_cards_idx]){
            elsie_cards_idx++;
            continue;
        }
        bessie_cards[bessie_cards_idx++] = num;
    }
    // for(auto b:bessie_cards) cout << b << '\n';

    // ans 계산
    int ans = 0;
    bessie_cards_idx = 0;

    for(auto e:elsie_cards){
        while (e > bessie_cards[bessie_cards_idx])
            bessie_cards_idx ++;
            if(bessie_cards_idx >= N) break;

        if(bessie_cards_idx >= N) break;
        ans++;
        bessie_cards_idx++;
    }

    cout << ans;
}