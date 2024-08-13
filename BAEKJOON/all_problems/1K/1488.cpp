#include <iostream>
using namespace std;

int main(void){
    int ca, cb, maxa, maxb;
    cin >> ca >> cb >> maxa >> maxb;

    // if(maxa == 0 and maxb == 0){
    //     cout << 0;
    //     return 0;
    // }
    if(maxa == 0){
        cout << min(cb, maxb);
        return 0;
    }
    if(maxb == 0){
        cout << min(ca, maxa);
        return 0;
    }

    // na: a로만 이루어진 부분문자열(그룹)의 개수
    int na = ca/maxa, nb = cb/maxb;
    if(ca%maxa) na += 1;
    if(cb%maxb) nb += 1;

    if(abs(na-nb) <= 1){
        cout << ca + cb;
    } else if (na<nb) {             // nb > na+1
        na = min(ca, nb);
        if((na == nb) or ((na+1) == nb)){
            cout << ca + cb;
        } else {
            cout << ca + maxb*(na+1);
        }
    } else{                         // na > nb+1
        nb = min(cb, na);
        if((nb == na) or ((nb+1) == na)){
            cout << cb + ca;
        } else {
            cout << cb + maxa*(nb+1);
        }
    }
}