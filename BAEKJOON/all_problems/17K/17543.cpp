#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int n; cin >> n;
    // cout << "n : " << n << '\n';

    string s;
    getline(cin, s);
    getline(cin, s);

    stringstream ss(s);
    string t;

    ll ans = 0;
    ll mod = int(1e9)+7;
    stack<ll> stack_ll({0});
    ll flag_plus = true;
    bool get_stack_num = false;
    // cout << stack_ll.top();

    while(getline(ss, t, ' ')){
        if(t == "("){
            flag_plus = !flag_plus;
            if(flag_plus)   stack_ll.push(0);
            else            stack_ll.push(1);
        }
        else if(t == ")"){
            flag_plus = !flag_plus;

            ll tmp = stack_ll.top(); stack_ll.pop();
            if(flag_plus)   stack_ll.top() = (stack_ll.top()+tmp)%mod;
            else            stack_ll.top() = (stack_ll.top()*tmp)%mod;
        }
        else{
            ll k = stoll(t);
            if(flag_plus)   stack_ll.top() = (stack_ll.top()+k)%mod;
            else            stack_ll.top() = (stack_ll.top()*k)%mod;
        }
    }

    cout << stack_ll.top();
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}