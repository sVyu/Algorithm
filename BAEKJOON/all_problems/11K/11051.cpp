// 꼭 작동하도록 해보자
// #include <iostream>
// using namespace std;

// int mod = int(1e4)+7;

// int f(int n){
//     int val = 1;
//     for(int k=2; k<=n; k++){
//         val = (val*k)%mod;
//     }
//     return val;
// }

// int main(void){
//     int N, K;
//     cin >> N >> K;

//     int val = 1;
//     for(int tmp=N; tmp>(N-K); tmp--){
//         val = (val*tmp);
//     }
//     cout << val << '\n';

//     cout << val/f(K);

//     return 0;
// }