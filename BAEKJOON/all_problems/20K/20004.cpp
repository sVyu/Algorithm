#include <iostream>
using namespace std;

int main(void){
    int A = 0;
    cin >> A;

    for(int i=1; i<A+1; i++){
        if(30 % (i+1) == 0) cout << i << '\n';
    }
}