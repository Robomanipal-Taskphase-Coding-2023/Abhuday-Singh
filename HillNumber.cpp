#include <iostream>
#include <vector>
using namespace std;

void hillnum(void) {

	cout << "Enter number\n";
	int n;
	cin >> n;

	vector<int> a(0);
	while (n > 0) {
		a.insert(a.begin(), n % 10);
		n /= 10;
	}

	int stateswitch = 0;
	bool asc = true;
	for (int i = 0; i < a.size() - 1; i++) {
		int j = i + 1; //gets rid of a weird warning
		if (a[i] == a[j] || stateswitch > 1) {
			cout << "not a hillnum\n";
			exit(0);
		}
		if ((asc && a[i] > a[j]) || (!asc && a[i] < a[j])) {
			asc = !asc;
			stateswitch += 1;
		}
	}

	if (stateswitch == 1) {
		cout << "hillnumber.\n";
	}
	else {
		cout << "not a hillnumber\n";
	}

	return;
}
