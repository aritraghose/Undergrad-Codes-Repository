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
vector<vector<int> > ed = {{0,1},{0,2},{1,2},{3,4}};

vector<int> root;
vector<int> members;
vector<int> edges;
vector<int> ranks;

// Quick Union

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
        	members[root_x] += members[root_y];
        	edges[root_x] += (edges[root_y] + 1);

    	} else if (ranks[root_x] < ranks[root_y]) {
        	root[root_x] = root_y;
        	members[root_y] += members[root_x];
        	edges[root_y] += (edges[root_x]+1);
    	} else {
        	root[root_y] = root_x;
        	ranks[root_x]++;
        	members[root_x] += members[root_y];
        	edges[root_x] += (edges[root_y]+1);
    	}
	} else {
		if (ranks[root_x] > ranks[root_y]) {
        	edges[root_x] += 1;
		} else if (ranks[root_x] < ranks[root_y]) {
        	edges[root_y] += 1;
    	} else {
        	edges[root_x] += 1;
    	}
	}
}


void solve() {
	int nodes;
	cin >> nodes;
	nodes = 6;
	for (int i=0; i < nodes; i++) {
    	root.push_back(i);
    	ranks.push_back(1);
    	members.push_back(1);
    	edges.push_back(0);
	}
	for (int i=0; i < ed.size(); i++) {
		join(ed[i][0], ed[i][1]);
	}




	int count = 0;
	for (int i=0; i < nodes; i++) {
    	if (root[i] == i) {
    		if (((members[i]*(members[i]-1))/2) == edges[i]) {
    			count++;
    		}
    	}
	}


	cout << count;


}


int main() {
	init_code();
	int t = 1;
	//cin >> t;
	while(t--) solve();
	return 0;
}
