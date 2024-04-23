// #include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int genders = 2, grades = 7;
    int B[genders][grades];
    for(int i = 0; i < genders; i++){
        fill_n(B[i], grades, 0);
    }

    // // test if 'reset' is working or not by cout 
    // for(int x = 0; x < genders; x++){
    //     for(int y = 0; y < grades; y++){
    //         cout << B[x][y] << ' ';
    //     }
    //     cout << '\n';
    // }

    int n, k;
    cin >> n >> k;
    for(int i = 0; i < n; i++){
        int gender, grade;
        cin >> gender >> grade;
        // cout << "test " << gender << grade << '\n';
        // cout << 'what???' << '\n';
        B[gender][grade] += 1;
    }

    int ans = 0;
    for(int x = 0; x < genders; x++){
        for(int y = 0; y < grades; y++){
            ans += B[x][y] / k;
            if(B[x][y] % k) ans += 1;
        }
    }
    cout << ans;

    return 0;
}