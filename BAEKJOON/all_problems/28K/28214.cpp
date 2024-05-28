#include <iostream>
using namespace std;

int main(void){
    int ans=0;
    int N, K, P;
    int cream;
    cin >> N >> K >> P;

    for(int i=0; i<N; i++){
        int no_cream = 0;
        for(int j=0; j<K; j++){
            cin >> cream;
            if(!cream) no_cream += 1;
        }
        if(no_cream < P) ans += 1;
    }
    cout << ans << '\n';

    return 0;
}