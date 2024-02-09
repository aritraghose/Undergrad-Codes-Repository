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
    int t = 50;
    string prev = "none";
    while (true) {
        char s[30];
        cin >> s;
        cout << fixed;
        cout << setprecision(3);
        double h = 0.000, m = 0.000, angle = 0.000;;
        bool hour = false;
        cout << setprecision(3);
        int i = 0;
        while (s[i] != '\0') {
            if (s[i] == ':') {
                hour = true;
            } else if (!hour) {
                h = (h*10.000) + (int(s[i])-48.000);
            } else if (hour) {
                m = (m*10.000) + (int(s[i])-48.000);
            }
            i++;
        }
        if ((h == 0.000) and (m == 0.000)) {   
            break;
        } else {
            angle += (h*30.000);
            angle += ((m/60.000)*30.000);
            angle -= (m*6.000);
            if (angle < 0.000) {
                angle *= -1.000;
            }
            if (angle > 180.000) {
                angle = 360.000 - angle;
            }
            cout << angle << endl;

        }

    }
    // ----------------------------------------------------------------
    return 0;
}