#include <iostream>
#include "helpers.h"
using namespace std;

void swap(char** sptr, char** tptr) {
	char* temp = *sptr;
	*sptr = *tptr;
	*tptr = temp;
}

void strsort(void) {
	cout << "How many strings?\n";
	int n;
	cin >> n;
	char** a = new char* [n];
	int* l = new int[n];
	cout << "Enter strings (l<100)\n";
	for (int i = 0; i < n; i++) {
		a[i] = new char[100];
		cin >> a[i];
		for (int j = 0; j < 100; j++) {
			if (a[i][j] == '\0') {
				l[i] = j;
				break;
			}
			a[i][j] = tolower(a[i][j]);
		}
	}

	int min;
	int temp = 0;
	for (int i = 0; i < n; i++) {
		min = i;
		for (int j = i + 1; j < n; j++) {
			if (l[j] < l[min]) {
				min = j;
			}
		}
		temp = l[min];
		l[min] = l[i];
		l[i] = temp;

		swap(a[i], a[min]);
	}

	cout << "array sorted by string length is:\n";
	for (int i = 0; i < n; i++) {
		cout << a[i] << endl;
		alphasort(a[i], l[i]);
	}

	cout << "array with each string sorted alphabetically is:\n";
	for (int i = 0; i < n; i++) {
		cout << a[i] << endl;
	}
}
