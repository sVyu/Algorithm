#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s;
    getline(cin, s);
    // getline(cin, s, '\n');

    while(!cin.eof()) {
        cout << s << '\n';
        getline(cin, s);
    }
    return 0;
}