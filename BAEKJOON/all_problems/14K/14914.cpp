#include <iostream>
using namespace std;

int main()
{
    int a=0,b=0;
    cin >> a >> b;
    for(int i=1; i<=min(a,b); i++){
        if(a%i == 0 & b%i == 0){
            cout << i << " " << a/i << " " << b/i << endl;
        }
    }
}