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
    int t = 1; //cin >> t;
    while (t--) {
        int n = 100, correct = 0;
        string prev = "next";
        while (n--) {
            char s[30];
            cin >> s;
            if (s != prev) {
                prev = s;
            } else {
                continue;
            }
            int a = 0, b = 0, c = 0;
            char o;
            bool first = false, second = false, ans = false, op = false, eq = false, wrong = false, neg = false;

            for (int i=0; i<strlen(s); i++) {
                if (!first && !second && !ans && !op && !eq) {
                    if ((s[i] == '+') or (s[i] == '-')) {
                        first = true;
                        o = s[i];
                    } else {
                        a = (a*10) + (int(s[i])-48);
                    }
                } else if (!second && !ans && !eq) {
                    if (s[i] == '=') {
                        second = true;
                        eq = true;
                    } else {
                        b = (b*10) + (int(s[i])-48);
                    }
                } else if (eq) {
                    if (s[i] == '?') {
                        wrong = true;
                    } else if (s[i] == '-') {
                        neg = true;
                    } else {
                        c = (c*10) + (int(s[i])-48);
                    }
                }
            }
            if (!wrong) {
                if (neg) {
                    c = -1*c;
                }
                if ((o == '+') and (a+b == c)) {
                    correct++;
                    //cout << a << o << b << "  =  " << c << endl; 
                } else if (((o == '-') and (a-b == c))) {
                    correct++;
                    //cout << a << o << b << "  =  " << c << endl; 
                }
            }
        }
        cout << correct << endl;
    }
    // ----------------------------------------------------------------
    return 0;
}