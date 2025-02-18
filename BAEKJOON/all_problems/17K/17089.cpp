#include <bits/stdc++.h>
using namespace std;
#define pii pair<int, int>

int main(void){
    int n, m; cin >> n >> m;

    int relations[n+1][n+1];
    fill(&relations[0][0], &relations[0][0]+(n+1)*(n+1), 0);

    queue<pii> q;
    for(int i=0; i<m; ++i){
        int a, b; cin >> a >> b;
        relations[a][b] = 1;
        relations[b][a] = 1;
        q.push({a, b});
    }

    // sums init
    int sums[n+1];
    fill(sums, sums+(n+1), 0);

    for(int i=1; i<=n; ++i){
        int sum = 0;
        for(int j=1; j<=n; ++j) sum += relations[i][j];
        sums[i] = sum;
    }

    // for(int i=1; i<=n; ++i){
    //     cout << sums[i] << '\n';
    // }

    // 2�� for�� ������ �̸� �����ؾ� ����
    // next permutation ����� �� �� �������� �����ϸ� ���� ��
    // �ִ��� �ƴ϶� �ּڰ��̾��ٴ�

    int ans = INT_MAX;
    while(!q.empty()){
        auto [a, b] = q.front(); q.pop();
        for(int i=1; i<=n; ++i){
            if(i == a | i == b) continue;
            if(relations[a][i] and relations[b][i]){
                ans = min(ans, sums[a]+sums[b]+sums[i]-6);
            }
        }
    }

    if(ans == INT_MAX) ans = -1;
    cout << ans;
}

