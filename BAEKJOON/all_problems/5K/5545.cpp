#include <iostream>
#include <algorithm>
using namespace std;

bool compare(int a, int b){
    return a > b;
}

int main(void){
    int N, A, B, C;
    cin >> N >> A >> B >> C;

    int dough[N] = {0};
    for(int i=0; i<N; i++){
        cin >> dough[i];
    }
    sort(dough, dough+N, compare);

    int tot_cal = C, tot_price = A;
    for(auto d:dough){
        if(int(tot_cal/tot_price) > int((tot_cal+d)/(tot_price+B)))
            break;
        tot_cal += d;
        tot_price += B;
    }

    cout << tot_cal/tot_price;
}