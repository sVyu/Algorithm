#include <iostream>
using namespace std;

int main(void){
    bool pos = true;
    int n;

    for(int i=0; i<8; i++){
        cin >> n;
        if(n!=0 and n!=1){
            pos = false;
            break;
        }
    }

    if(pos) cout << 'S';
    else cout << 'F';
}