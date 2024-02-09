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

int N = 1000;

// Dijkstra Function

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

void findPath(int node) {
    if (node == -1)  {
        return;
    }
    cout << node << " ";
    findPath(parent[node]);
}




int main() {
   init_code();
   int t = 1;
   //cin >> t;
   while(t--) {

    // Problem 2:     Dijkstra (with path)
        
    int nodes, edges;
    cin >> nodes >> edges;
    while (edges--) {
        int u, v, w;
        cin >> u >> v >> w;
        graph_d[u].push_back(make_pair(v, w));
        graph_d[v].push_back(make_pair(u, w));

    }
    dijkstra(1);
    for (int i = 1; i <= nodes; i++) {
        cout << i << ": " << distances_d[i] << endl;
        cout << "Path: ";
        findPath(i);
        cout << endl << endl;


    }

   }



   return 0;
}
