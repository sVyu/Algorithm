#include <bits/stdc++.h>
using namespace std;

struct edge{
    int v; int dist;
    edge(int v, int dist): v(v), dist(dist){}
};

struct cmp{
    bool operator()(edge a, edge b){
        return a.dist > b.dist;
    }
};

int solve(){
    int V, E;
    cin >> V >> E;

    int s; cin >> s;
    bool visited[V+1];
    fill(&visited[0], &visited[0]+(V+1), false);
    int d[V+1];
    fill(&d[0], &d[0]+(V+1), INT_MAX);

    vector<vector<edge>> g(V+1, vector<edge>());
    priority_queue<edge, vector<edge>, cmp> pq;
    for(int i=0; i<E; i++){
        int u, v, d;
        cin >> u >> v >> d;
        g[u].push_back({v, d});
    }

    for(auto e:g[s]) pq.push(edge(e.v, e.dist));
    visited[s] = true;
    d[s] = 0;

    while(!pq.empty()){
        edge e = pq.top(); pq.pop();
        if(!visited[e.v]){
            visited[e.v] = true;
            d[e.v] = e.dist;

            for(auto ne:g[e.v]){
                if(!visited[ne.v]){
                    pq.push(edge(ne.v, e.dist+ne.dist));
                }
            }
        }
    }

    for(int i=1; i<=V; i++){
        if(d[i] == INT_MAX) cout << "INF\n";
        else                cout << d[i] << '\n';
    }

    return 0;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}