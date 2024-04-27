// [바킹독의 실전 알고리즘] 0x04강 - 연결 리스트
// https://youtu.be/C6MX5u7r72E?si=vnpceja9leEuQsPH

#include <bits/stdc++.h>
using namespace std;

const int max_len = int(1e6);
vector<char> dat(max_len);
vector<int> pre(max_len, -1), nxt(max_len, -1);
int unused = 1;

void insert(int addr, int num){
    dat[unused] = num;
    pre[unused] = addr;
    nxt[unused] = nxt[addr];
    if(nxt[addr] != -1) pre[nxt[addr]] = unused;
    nxt[addr] = unused;
    unused++;
}

void erase(int addr){
    nxt[pre[addr]] = nxt[addr];
    if(nxt[addr] != -1) pre[nxt[addr]] = pre[addr];
}

void traversal(){
    int cur = nxt[0];
    while(cur != -1){
        cout << dat[cur];
        cur = nxt[cur];
    }
    // cout << "\n";
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string init;
    cin >> init;
    // int cursor = init.length();
    int cursor = 0;

    for(auto c:init){
        insert(cursor, c);
        cursor++;
    }

    int m;
    cin >> m;
    // for(int i=0; i<m; i++){
    while(m--){
        char cmd;
        cin >> cmd;

        if(cmd == 'P'){
            char val;
            cin >> val;
            insert(cursor, val);
            cursor = nxt[cursor];
        }
        else if(cmd == 'L'){
            if(pre[cursor] != -1){
                cursor = pre[cursor];
            }
        }
        else if(cmd == 'D'){
            if(nxt[cursor] != -1){
                cursor = nxt[cursor];
            }
        }
        else if(cmd == 'B'){
            if(cursor){ // cursor != 0
                erase(cursor);
                cursor = pre[cursor];
            }
        }
    }
    traversal();

    return 0;
}