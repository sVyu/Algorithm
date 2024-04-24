#include <iostream>
#include <vector>
#include <algorithm>
// #include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int a, b;
    const int max_cards_index = 21;
    // int cards[21] = {0,};
    vector<int> cards(max_cards_index, 0);
    for(int i = 1; i < max_cards_index; i++){
        cards[i] = i;
    }

    int l, r;
    for(int i = 0; i < 10; i++){
        cin >> l >> r;
        int nl = l, nr = r;

        while(nl < nr){
            swap(cards[nl], cards[nr]);
            nl += 1;
            nr -= 1;
        }
    }

    for(int i = 1; i < max_cards_index; i++){
        cout << cards[i] << ' ';
    }

    return 0;
}
