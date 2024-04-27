#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    string init;
    cin >> init;

    int m;
    cin >> m;

    stack<char> pre, now;
    for(auto c:init) pre.push(c);

    char op;
    while(m--){
        cin >> op;
        if(op == 'L'){
            if(!pre.empty()) {
                now.push(pre.top());
                pre.pop();
            }
        }
        else if(op == 'D'){
            if(!now.empty()){
                pre.push(now.top());
                now.pop();
            }
        }
        else if(op == 'B'){
            if(!pre.empty()){
                pre.pop();
            }
        }
        else { // op == 'P'
            char val;
            cin >> val;
            pre.push(val);
        }
    }

    // Ãâ·ÂºÎ
    while(!pre.empty()){
        now.push(pre.top());
        pre.pop();
    }
    while(!now.empty()){
        cout << now.top();
        now.pop();
    }
}