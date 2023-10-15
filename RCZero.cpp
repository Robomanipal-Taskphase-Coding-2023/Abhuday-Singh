#include <iostream>
#include "helpers.h"
using namespace std;

void rczero(void) {

	int ra, ca;
	cout << "Enter rows and columns in array\n";
	cin >> ra >> ca;

	bool** tz = new bool* [ra];
	for (int i = 0; i < ra; i++) {
		tz[i] = new bool[2];
		for (int j = 0; j < 2; j++) {
			tz[i][j] = false;
		}
	}

	cout << "Enter matrix row-wise\n";
	int** a = new int* [ra];
	for (int i = 0; i < ra; i++) {
		a[i] = new int[ca];
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
			if (tz[j][1] || tz[i][0]) {
				a[i][j] = 0;
			}
		}
	}

	cout << "Adjusted matrix is:\n";
	intmatprint(a, ra, ca);
}
