// #include <bits/stdc++.h>
// using namespace std;

// void solve(){
//     int n; cin >> n;
//     vector<int> zs(n); for(auto &z:zs) cin >> z;
//     int tot = accumulate(zs.begin(), zs.end(), 0);

//     int ans[n] = {0,};
//     for(int val=1; val<=tot; ++val){
//         if((tot % val) != 0) continue;

//         int cnt = 0;
//         int now = 0;
//         for(int z:zs){
//             now = (now+z) % val;
//             if(now != 0) ++cnt;
//         }
//         ans[cnt] = val;
//     }

//     // for(int i=1; i<n; ++i) if(ans[i] == 0) ans[i] = ans[i-1];
//     for(int i=1; i<n; ++i) ans[i] = max(ans[i], ans[i-1]);
//     for(int a:ans) cout << a << ' ';
// }

// int main(void){
//     ios::sync_with_stdio(0);
//     cin.tie(0);
//     solve();
//     return 0;
// }


/*
line
*/

// #include <bits/stdc++.h>
// using namespace std;

// vector<int> solve1(vector<int> zs){
//     // int n; cin >> n;
//     // vector<int> zs(n); for(auto &z:zs) cin >> z;
//     int tot = accumulate(zs.begin(), zs.end(), 0);

//     vector<int> ans(5, 0);
//     for(int val=1; val<=tot; ++val){
//         if((tot % val) != 0) continue;

//         int cnt = 0;
//         int now = 0;
//         for(int z:zs){
//             now = (now+z) % val;
//             if(now != 0) ++cnt;
//         }
//         ans[cnt] = val;
//     }

//     for(int i=1; i<5; ++i) if(ans[i] == 0) ans[i] = ans[i-1];
//     // for(int a:ans) cout << a << ' ';
//     return ans;
// }

// vector<int> solve2(vector<int> zs){
//     // int n; cin >> n;
//     // vector<int> zs(n); for(auto &z:zs) cin >> z;
//     int tot = accumulate(zs.begin(), zs.end(), 0);

//     vector<int> ans(5, 0);
//     for(int val=1; val<=tot; ++val){
//         if((tot % val) != 0) continue;

//         int cnt = 0;
//         int now = 0;
//         for(int z:zs){
//             now = (now+z) % val;
//             if(now != 0) ++cnt;
//         }
//         ans[cnt] = val;
//     }

//     for(int i=1; i<5; ++i) ans[i] = max(ans[i], ans[i-1]);
//     // for(int a:ans) cout << a << ' ';
//     return ans;
// }


// int main(void){
//     ios::sync_with_stdio(0);
//     cin.tie(0);

//     while(true){
//         vector<int> base(5, 0);
//         for(int i=0; i<5; ++i){
//             base[i] = rand() % 10;
//         }

//         vector<int> a = solve1(base);
//         vector<int> b = solve2(base);

//         bool find = false;
//         for(int i=0; i<5; ++i){
//             if(a[i] != b[i]){
//                 find = true;
//                 break;
//             }
//         }

//         if(find){
//             for(int i=0; i<5; ++i) cout << base[i] << ' ';
//             cout << '\n';
//             for(int i=0; i<5; ++i) cout << a[i] << ' ';
//             cout << '\n';
//             for(int i=0; i<5; ++i) cout << b[i] << ' ';
//             cout << '\n';
//             break;
//         }
//     }

//     return 0;
// }