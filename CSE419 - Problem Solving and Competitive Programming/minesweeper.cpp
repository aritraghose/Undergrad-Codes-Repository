#include<bits/stdc++.h>
#define ll long long
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)
using namespace std;

void init_code() {
    fast_io;
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
}


int main() {
    init_code();
    // -----------------------------------------------------------------
    int tc = 1;
    while (true) {
        int n, m;
        cin >> n >> m;
        if ((n == 0) and (m == 0)) {
            break;
        }
        vector<string> grid;

        for (int i=0; i<n; i++) {
            string s;
            cin >> s;
            grid.push_back(s);
        }
        if (tc > 1) {
            cout << endl;
        }
        cout << "Field #" << tc << ":" << endl;
        tc++;

        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                int count = 0;
                if (grid[i][j] != '*') {
                    if (i-1 != -1) {
                        if (grid[i-1][j] == '*') {
                            count++;
                        }
                    }
                    if (i+1 != n) {
                        if(grid[i+1][j] == '*') {
                            count++;
                        }
                    }
                    if (j-1 != -1) {
                        if(grid[i][j-1] == '*') {
                            count++;
                        }
                    }
                    if (j+1 != m) {
                        if(grid[i][j+1] == '*') {
                            count++;
                        }
                    }
                    if ((i-1 != -1) and (j-1 != -1)) {
                        if(grid[i-1][j-1] == '*') {
                            count++;
                        }
                    }
                    if ((i-1 != -1) and (j+1 != m)) {
                        if(grid[i-1][j+1] == '*') {
                            count++;
                        }
                    }
                    if ((i+1 != n) and (j-1 != -1)) {
                        if(grid[i+1][j-1] == '*') {
                            count++;
                        }
                    }
                    if ((i+1 != n) and (j+1 != m)) {
                        if(grid[i+1][j+1] == '*') {
                            count++;
                        }
                    }

                    cout << count;

                } else {
                    cout << '*';
                }

            }
            cout << endl;
        }



    }
    // ----------------------------------------------------------------
    return 0;
}