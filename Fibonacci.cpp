#include <iostream>
using namespace std;

static constexpr int N = 40;
int map[N];

//approx. execution time: 0 seconds
int fibonacci(int n) {

	if (n <= 1) {
		return n;
	}

	if (map[n - 1] != -1) {
		return map[n - 1];
	}

	int fib = fibonacci(n - 1) + fibonacci(n - 2);
	map[n - 1] = fib;
	return fib;
}

void fibonacci(void) {

	time_t start, end;
	time(&start);

	for (int i = 1; i < N; i++) {
		map[i] = -1;
	}

	for (int i = 1; i <= N; i++) {
		cout << fibonacci(i) << endl;
	}

	time(&end);
	int exetime = int(end - start);

	cout << "\nExecution time: " << exetime << " sec\n";
}
