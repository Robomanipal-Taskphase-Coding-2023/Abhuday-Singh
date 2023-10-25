#include <iostream>
using namespace std;

// Function to print a matrix
void matprint(int** matrix, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cout << matrix[i][j] << ' ';
        }
        cout << endl;
    }
}

void rczero() {
    int ra, ca;
    cout << "Enter rows and columns in the array: ";
    cin >> ra >> ca;

    bool** tz = new bool*[ra];
    for (int i = 0; i < ra; i++) {
        tz[i] = new bool[2];
        tz[i][0] = false; // Initialize to false
        tz[i][1] = false;
    }

    int** a = new int*[ra];
    for (int i = 0; i < ra; i++) {
        a[i] = new int[ca];
    }

    cout << "Enter matrix row-wise:\n";
    for (int i = 0; i < ra; i++) {
        for (int j = 0; j < ca; j++) {
            cin >> a[i][j];
            if (a[i][j] == 0) {
                tz[i][0] = true;
                tz[j][1] = true;
            }
        }
    }

    for (int i = 0; i < ra; i++) {
        for (int j = 0; j < ca; j++) {
            if (tz[i][0] || tz[j][1]) {
                a[i][j] = 0;
            }
        }
    }

    cout << "Adjusted matrix is:\n";
    matprint(a, ra, ca);
}

int main() {
    rczero();
    return 0;
}
