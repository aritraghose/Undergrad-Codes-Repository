#include<bits/stdc++.h>
#include <cstdint>
#define ll long long
#define fast_io ios_base::sync_with_stdio(0);cout.tie(nullptr);cin.tie(nullptr);
#define nl "\n"
#define pb push_back
#define fr(i,a,b) for(int i = a; i < b; i++)
#define mod 1000000007
#define inf (1LL<<60)
#define all(x) (x).begin(), (x).end()
#define prDouble(x) cout << fixed << setprecision(10) << x
#define triplet pair<ll,pair<ll,ll>>
#define read(x) int x; cin >> x
using namespace std;

void init_code() {
	fast_io;
	#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif
}

int N = 50;

vector<int> root;
vector<int> ranks;

// Union by Rank with Path Compression

int find(int v) {
	if (root[v] == v) return v;
	root[v] = find(root[v]);
	return root[v];
}


void join(int x, int y) {
	int root_x = find(x);
	int root_y = find(y);

	if (root_x != root_y) {
    	if (ranks[root_x] > ranks[root_y]) {
        	root[root_y] = root_x;
    	} else if (ranks[root_x] < ranks[root_y]) {
        	root[root_x] = root_y;
    	} else {
        	root[root_y] = root_x;
        	ranks[root_x]++;
    	}
	}
}

void solve() {
	int nodes, edges;
	cin >> nodes >> edges;
	for (int i=0; i <= nodes; i++) {
    	root.push_back(i);
    	ranks.push_back(1);
	}
	while (edges--) {
    	int x, y;
    	cin >> x >> y;
    	join(x, y);
	}



	// printing root and ranks array
	int count = 0;
	vector<pair<int, int>> newRoads;
	int x = 0;
	pair<int, int> y;
	for (int i=1; i <= nodes; i++) {
		if (root[i] == i) {
			count++;
			if (x == 0) {
				y.first = i;
				x = 1;
			} else {
				y.second = i;
				newRoads.push_back(y);
				y.first = i;
			}
		}

	}
	cout << count-1 << endl;

	for (int i=0; i < newRoads.size(); i++) {
		cout << newRoads[i].first << " " << newRoads[i].second << endl;
	}

}


int main() {
	init_code();
	int t = 1;
	//cin >> t;
	while(t--) solve();
	return 0;
}
