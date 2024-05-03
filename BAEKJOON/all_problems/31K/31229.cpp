#include <iostream>
#include <cmath>
using namespace std;

bool prime_check(int k){
    if(k==1) return false;
    else if(k==2) return true;
    else if(k%2 == 0) return false;
    else{
        for(int i=3; i<=int(sqrt(k)); i+=2){
            if(k%i == 0) return false;
        }
        return true;
    }
}

int main(void){
    int n;
    cin >> n;

    int k=2;
    while(n){
        if(prime_check(k)){
            cout << k << ' ';
            n--;
        }
        k += 1;
    }
}