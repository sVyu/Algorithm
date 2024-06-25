#include <iostream>
using namespace std;
typedef long long ll;

int main(void){
    ll w, h, p, q, t;
    cin >> w >> h >> p >> q >> t;

    cout << w-abs(w-((p+t) % (2*w))) << ' ' << h-abs(h-((q+t) % (2*h)));
}