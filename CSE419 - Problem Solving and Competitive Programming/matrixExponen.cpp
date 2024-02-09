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

const int N = 100;
const int mod = 1e9+7;
/*
We will be using a structure for matrix. You can also use a simple 2 dimensional array as a matrix.
However, if you create a structure you can always reuse this structure if you once clearly understand
how it has been designed. Please take some time to understand the following structure.
*/
struct Matrix{
    int row,col;
    long long int m[N][N];

    // Constructor for the structure Matrix
    Matrix(int row_num, int col_num)
    {
        row = row_num;
        col = col_num;
        // Initializing with a zero matrix
        for(int i=0;i<row;i++)
        {
            for(int j=0; j<col;j++)
            {
                m[i][j] = 0;
            }
        }
    }

    // Overloading the multiplication operator
    Matrix operator*(Matrix B){
        Matrix product(row, B.col);
        // Product is initialized as a zero matrix
        // The following code is the basic matrix multiplication code
        for (int i=0; i < row; i++) {
            for (int j=0; j < B.col; j++) {
                for (int k=0; k < row; k++) {
                    product.m[i][j] = ((product.m[i][j]%mod) + ((((*this).m[i][k]%mod) *1ll* (B.m[k][j]%mod))%mod))%mod;
                }
            }
        }
        // Write the basic matrix multiplication code using three nested loops or you can also use Strassen's Matrix Multiplication Algorithm ;p
        
        return product;
    }
    // The iterative implementation of the fast exponentiation
    Matrix pow(long long int n)
    {
        Matrix ans(row,col);
        // ans is still a zero matrix
        for(int i=0;i<row;i++)
            ans.m[i][i] = 1;
        // ans is now the identity matrix

        Matrix a = (*this) * ans;
        // a is basically the original (*this) matrix, the matrix that is to be raised to the power of n.
        // The value of a will get changed but we will not be losing our original (*this) matrix.
        // Well you do not need to preserve the original matrix anyways. It's just a "Bhodrota".
        while(n)
        {
            if(n&1)
            {
                ans = ans*a;
            }
            a = a*a;
            n>>=1;
        }
        // Hope you recognize the while loop from our iterative implementation of fast exponentiation
        return ans; // Since ans is now holding the final answer.
    }

    void print_matrix() // This type of functions are prepared for debugging purposes mainly. You can print your matrix in any way you wish.
    {
        for(int i=0;i<row;i++)
        {
            for(int j=0;j<col;j++)
            {
                cout << m[i][j] << " ";
            }
            cout << endl;
        }
    }
};
 
int main()
{
    init_code();
    long long int n;
    cin >> n;
    Matrix Q(2,2);

    Q.m[0][0] = 0,     Q.m[0][1] = 1;
    Q.m[1][0] = 1,     Q.m[1][1] = 1;

    //Q.print_matrix();

    Matrix F(2,1);
    
    F.m[0][0] = 0;
    F.m[1][0] = 1;

    //F.print_matrix();
    
    Matrix Qn = Q.pow(n);

    //Qn.print_matrix();

    Matrix Ans = Qn * F;

    cout << Ans.m[0][0] << endl;
    return 0;
 
}

/*
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

*/