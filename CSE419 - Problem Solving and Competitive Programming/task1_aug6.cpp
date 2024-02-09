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


//vector<vector<int>> isConnected = {{1,1,0},{1,1,0},{0,0,1}};
vector<vector<int>> isConnected = {{1,0,0},{0,1,0},{0,0,1}};
int N = isConnected.size() + 1;

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
	for (int i=0; i < N; i++) {
		root.push_back(i);
		ranks.push_back(1);
	}
	for (long unsigned int i=0; i < isConnected.size(); i++) {
		for (long unsigned int j=0; j < isConnected.size(); j++) {
			if (isConnected[i][j] == 1) {
				join(i+1, j+1);
			}
		}
	}


	int count = 0;
	for (int i=1; i < N; i++) {
		if (root[i] == i) count++;
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



