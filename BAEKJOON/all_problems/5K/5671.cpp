#include <iostream>
using namespace std;

int main(void){
    int n, m;
    while(true){
        cin >> n >> m;
        if(cin.eof()) break; //

        int ans = 0;
        for(int k=n; k<=m; k++){
            string sn = to_string(k);
            bool pos = true;
            int cnts[10] = {0};

            for(auto cn:sn){
                int target = int(cn)-48; // 
                if(cnts[target]){
                    pos = false;
                    break;
                }
                else cnts[target] += 1;
            }

            if(pos) ans += 1;
        }
        cout << ans << '\n';
    }
}