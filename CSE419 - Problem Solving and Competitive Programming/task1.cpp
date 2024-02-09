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



// BFS Function
int N = 1000;
vector<int> graph[1000];
vector<int> distances(N, 0);
vector<bool> visited(N, false);


void BFS(int source) {
	queue <int> pq;
	pq.push(source);
	visited[source] = true;

	while (pq.size() > 0) {
		int u = pq.front();
		pq.pop();
		for (int v : graph[u]) {
			if (visited[v] == false) {
				pq.push(v);
				visited[v] = true;
				distances[v] = distances[u] + 1;
			}
		}
	}
}



int main() {
   init_code();
   int t = 1;
   //cin >> t;
   while(t--) {


	// Problem 1:    BFS

   	int nodes, edges;
   	cin >> nodes >> edges;
   	while (edges--) {
   		int u, v;
   		cin >> u >> v;
   		graph[u].push_back(v);
   		graph[v].push_back(u);
   	}
   	BFS(1);

   	for (int i = 1; i <= nodes; i++) {
   		cout << i << ": " << distances[i] << endl;;
   	}
   }

   return 0;
}







