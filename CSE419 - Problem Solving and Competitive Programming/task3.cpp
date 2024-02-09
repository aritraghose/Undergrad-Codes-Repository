#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define fr(a,b) for(int i = a; i < b; i++)
#define rep(i,a,b) for(int i = a; i < b; i++)
#define mod 1e9+7
#define inf (1LL<<60)`
#define all(x) (x).begin(), (x).end()
#define prDouble(x) cout << fixed << setprecision(10) << x
#define triplet pair<ll,pair<ll,ll>>
#define goog(tno) cout << "Case #" << tno++ <<": "
#define fast_io ios_base::sync_with_stdio(0);cout.tie(nullptr);cin.tie(nullptr);
#define read(x) int x; cin >> x
#define nl "\n"
using namespace std;

void init_code(){
    fast_io;
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif 
}


// Dijkstra Function
int N = 1000;
vector<pair<int, int> > graph_d[1000];
vector<int> distances_d(N, 100000);
vector<int> parent(N, -1);

typedef pair<int, int> pi;
void dijkstra(int source) {

    distances_d[source] = 0;
    priority_queue<pi, vector<pi>, greater<pi> > q;
    q.push({0, source});

    while (!q.empty()) {
        int v = q.top().second;
        int dis_v = q.top().first;
        q.pop();
        if (dis_v != distances_d[v]) continue;

        for (auto edge: graph_d[v]) {
            int to = edge.first;
            int weight = edge.second;

            //cout << v << " " << to << "  " << weight << endl;
            if ((distances_d[v] + weight) < distances_d[to]) {
                distances_d[to] = distances_d[v] + weight;
            parent[to] = v;
            q.push({distances_d[to], to});
         }
        }




    }

}


int main() {
   init_code();
   int t = 1;
   while(t--) {
    // Problem 3
    int nodes, root;
    cin >> nodes >> root;
    int x = nodes-1;
    while (x--) {
        int u, v;
        cin >> u >> v;
        graph_d[u].push_back(make_pair(v, 1));
        graph_d[v].push_back(make_pair(u, 1));

    }
    dijkstra(root);

    int edgeNode = -1, bestDist = -1;

    for (int i=1; i < nodes+1; i++) {
        if (distances_d[i] > bestDist) {
            bestDist = distances_d[i];
            edgeNode = i;
        }
        distances_d[i] = 100000;
        parent[i] = -1;
    }

    dijkstra(edgeNode);
    int otherEdgeNode = -1;
    bestDist = -1;

    for (int i=1; i < nodes+1; i++) {
        if (distances_d[i] > bestDist) {
            bestDist = distances_d[i];
            otherEdgeNode = i;
        }
    }

    cout << "Farthest nodes: " << edgeNode << " " << otherEdgeNode;



   }

   return 0;
}


