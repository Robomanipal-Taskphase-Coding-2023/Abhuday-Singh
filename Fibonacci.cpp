#include <iostream>
using namespace std;

int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    cout << "The Fibonacci series is" << endl;
    for (int i = 0; i < 10; i++) {
        cout << fibonacci(i) << endl;
    }
    return 0;
}


